const rateLimitMap = new Map();

function isRateLimited(ip) {
  const now = Date.now();
  const windowMs = 60 * 1000; // 1 minute window
  const maxRequests = 5; // 5 requests per minute limit

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

function sanitizeInput(data) {
  if (typeof data === 'string') {
    return data
      .replace(/[<>]/g, '')
      .replace(/javascript:/gi, '')
      .trim();
  }
  if (typeof data === 'object' && data !== null) {
    for (const key in data) {
      if (Object.prototype.hasOwnProperty.call(data, key)) {
        data[key] = sanitizeInput(data[key]);
      }
    }
  }
  return data;
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, message: 'Method not allowed' });
  }

  const clientIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';

  if (isRateLimited(clientIp)) {
    return res.status(429).json({
      success: false,
      message: 'Too many requests. Please wait a minute before trying again.'
    });
  }

  const apiKey = process.env.WEB3FORMS_KEY || "a87235ca-05ef-406c-a0c1-c83def14c7c0";

  if (!apiKey) {
    return res.status(500).json({ success: false, message: 'Server configuration error: Missing API Key' });
  }

  try {
    let payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
    payload = sanitizeInput(payload);

    const response = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json', 
        'Accept': 'application/json' 
      },
      body: JSON.stringify({
        access_key: apiKey,
        ...payload
      })
    });

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    console.error("Secure API Route Error:", error);
    return res.status(500).json({ success: false, message: 'Failed to send email securely.' });
  }
}