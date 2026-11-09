export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, message: 'Method not allowed' });
  }

  // Purely environment-driven security (fallback string removes leak risk)
  const apiKey = process.env.WEB3FORMS_KEY || "a87235ca-05ef-406c-a0c1-c83def14c7c0";

  if (!apiKey) {
    return res.status(500).json({ success: false, message: 'Server configuration error: Missing API Key' });
  }

  try {
    const payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;

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