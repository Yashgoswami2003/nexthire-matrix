// Rate limiting map with dynamic memory cleanup
const rateLimitMap = new Map();

function isRateLimited(ip) {
  const now = Date.now();
  const windowMs = 60 * 1000; // 1 minute window
  const maxRequests = 10; // 10 AI generations per minute per IP

  if (rateLimitMap.size > 1000) {
    for (const [key, value] of rateLimitMap.entries()) {
      if (now - value.startTime > windowMs) {
        rateLimitMap.delete(key);
      }
    }
  }

  const userRecord = rateLimitMap.get(ip) || { count: 0, startTime: now };

  if (now - userRecord.startTime > windowMs) {
    userRecord.count = 1;
    userRecord.startTime = now;
  } else {
    userRecord.count++;
  }

  rateLimitMap.set(ip, userRecord);
  return userRecord.count > maxRequests;
}

function sanitizeInput(text) {
  if (typeof text !== 'string') return '';
  return text.trim();
}

// Fetch available Gemini API keys from environment
function getGeminiApiKeys() {
  const keys = [
    process.env.GEMINI_API_KEY_1,
    process.env.GEMINI_API_KEY_2,
    process.env.GEMINI_API_KEY_3,
    process.env.GEMINI_API_KEY_4,
    process.env.GEMINI_API_KEY_5,
    process.env.GEMINI_API_KEY_6,
  ].filter(key => key && key.trim().length > 0);

  return keys;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method Not Allowed' });
  }

  // Client IP Extraction for Vercel Serverless
  const rawIp = req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown';
  const clientIp = typeof rawIp === 'string' ? rawIp.split(',')[0].trim() : 'unknown';

  if (isRateLimited(clientIp)) {
    return res.status(429).json({
      success: false,
      error: 'Rate limit exceeded. Please wait a minute before making more requests.'
    });
  }

  try {
    let { prompt } = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    prompt = sanitizeInput(prompt);

    if (!prompt) {
      return res.status(400).json({ success: false, error: 'Prompt is required.' });
    }

    const apiKeys = getGeminiApiKeys();

    if (apiKeys.length === 0) {
      return res.status(500).json({ 
        success: false, 
        error: 'Server Error: No valid Gemini API keys configured in Vercel environment.' 
      });
    }

    let lastError = null;
    let aiResponseText = null;

    // Multi-Key Failover Engine Loop
    for (let i = 0; i < apiKeys.length; i++) {
      const selectedKey = apiKeys[i];
      
      // Supported models fallback (Flash -> Pro)
      const models = ['gemini-1.5-flash', 'gemini-1.5-pro'];

      for (const modelName of models) {
        try {
          const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${selectedKey}`;

          const geminiReq = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [{ text: prompt }]
              }]
            })
          });

          const geminiData = await geminiReq.json();

          if (geminiReq.ok && geminiData.candidates && geminiData.candidates[0]?.content?.parts[0]?.text) {
            aiResponseText = geminiData.candidates[0].content.parts[0].text;
            break; // Successfully got response
          } else {
            lastError = geminiData.error?.message || `Failed model attempt on ${modelName}`;
          }
        } catch (err) {
          lastError = err.message;
        }
      }

      if (aiResponseText) break; // Break key rotation if response generated
    }

    if (aiResponseText) {
      return res.status(200).json({ success: true, result: aiResponseText });
    } else {
      console.error("Gemini API Engine Failure:", lastError);
      return res.status(502).json({ 
        success: false, 
        error: 'AI Engine failover exhausted. Please try again in a few seconds.' 
      });
    }

  } catch (error) {
    console.error("Handler Error:", error);
    return res.status(500).json({ success: false, error: 'Internal Server Error.' });
  }
}