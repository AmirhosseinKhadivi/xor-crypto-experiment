<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>xor-crypto-experiment</title>
  <style>
    :root { color-scheme: light dark; }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      line-height: 1.55;
      margin: 0;
      padding: 24px;
      max-width: 980px;
    }
    header {
      padding: 18px 18px 10px;
      border: 1px solid rgba(127,127,127,.3);
      border-radius: 14px;
      margin-bottom: 18px;
    }
    h1 { margin: 0 0 6px; font-size: 28px; }
    .subtitle { margin: 0; opacity: .85; }
    .badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid rgba(127,127,127,.35);
      font-size: 12px;
      margin: 6px 6px 0 0;
      opacity: .95;
      text-decoration: none;
    }
    section {
      border: 1px solid rgba(127,127,127,.25);
      border-radius: 14px;
      padding: 16px 18px;
      margin: 14px 0;
    }
    h2 { margin: 0 0 10px; font-size: 18px; }
    code, pre {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
      font-size: 13px;
    }
    pre {
      overflow: auto;
      padding: 12px;
      border-radius: 12px;
      border: 1px solid rgba(127,127,127,.25);
      background: rgba(127,127,127,.08);
      margin: 10px 0 0;
      white-space: pre;
    }
    ul { margin: 8px 0 0 18px; }
    .warn {
      border-left: 6px solid #d97706;
      padding: 10px 12px;
      border-radius: 10px;
      background: rgba(217, 119, 6, .12);
    }
    .danger {
      border-left: 6px solid #dc2626;
      padding: 10px 12px;
      border-radius: 10px;
      background: rgba(220, 38, 38, .10);
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }
    @media (min-width: 860px) {
      .grid { grid-template-columns: 1fr 1fr; }
    }
    footer { margin-top: 18px; opacity: .8; font-size: 13px; }
    a { color: inherit; }
  </style>
</head>

<body>
  <header>
    <h1>xor-crypto-experiment</h1>
    <p class="subtitle">
      A small Tkinter GUI that demonstrates a repeating-key XOR cipher for learning and experimentation.
    </p>
    <div>
      <span class="badge">Python</span>
      <span class="badge">Tkinter GUI</span>
      <span class="badge">XOR Cipher</span>
      <span class="badge">Educational</span>
      <span class="badge">Offline-built</span>
    </div>
  </header>

  <section>
    <h2>Overview</h2>
    <p>
      This repository contains a simple GUI tool that encrypts/decrypts text using a repeating-key XOR operation.
      It was created as an <strong>offline learning exercise</strong> to explore basic ideas behind symmetric ciphers,
      encoding, and reversible transformations.
    </p>

    <div class="danger">
      <strong>Security Notice:</strong>
      This implementation is <strong>not cryptographically secure</strong> and must <strong>not</strong> be used to protect
      real data. Repeating-key XOR is vulnerable to multiple known attacks.
    </div>
  </section>

  <section>
    <h2>What this project demonstrates</h2>
    <div class="grid">
      <div>
        <ul>
          <li>How XOR can be used to build a reversible transform</li>
          <li>Why key reuse and short keys are dangerous</li>
          <li>How simple design decisions affect usability (e.g., output encoding)</li>
          <li>Basic GUI wiring with Tkinter</li>
        </ul>
      </div>
      <div class="warn">
        <strong>Tip:</strong>
        XOR output may include non-printable characters. For real usability, ciphertext is usually represented using
        <em>hex</em> or <em>base64</em> before displaying or saving.
      </div>
    </div>
  </section>

  <section>
    <h2>Project structure</h2>
    <pre>
xor-crypto-experiment/
├── app.py              (Tkinter GUI + XOR encrypt/decrypt)
└── README.html         (this file)
    </pre>
  </section>

  <section>
    <h2>How to run</h2>
    <p><strong>Requirements:</strong> Python 3.x (Tkinter included by default on most systems)</p>
    <pre>
python app.py
    </pre>
    <p>
      Choose <strong>Encrypt</strong> or <strong>Decrypt</strong>, enter a text and a key, then click the button.
    </p>
  </section>

  <section>
    <h2>How it works (high level)</h2>
    <p>
      XOR encryption here applies the XOR operation between each character of the text and a character of the key.
      When the key is shorter than the text, the key repeats (repeating-key XOR).
    </p>
    <pre>
cipher[i] = plain[i] XOR key[i mod key_length]
plain[i]  = cipher[i] XOR key[i mod key_length]
    </pre>
    <p>
      Because XOR is its own inverse, the same operation can encrypt and decrypt.
    </p>
  </section>

  <section>
    <h2>Recommended next steps</h2>
    <ul>
      <li>Represent ciphertext as <strong>hex</strong> or <strong>base64</strong> for safe display/copy/paste</li>
      <li>Separate UI from core logic into modules</li>
      <li>Compare with a modern AEAD scheme (e.g., AES-GCM) in a separate repository</li>
    </ul>
  </section>

  <section>
    <h2>License</h2>
    <p>
      Choose a license if you plan to share/reuse the code publicly (MIT is a common default).
    </p>
  </section>

  <footer>
    <p>
      <strong>Disclaimer:</strong> Educational code. No security guarantees.
      If you need real encryption, use modern vetted primitives (e.g., AES-GCM via the <code>cryptography</code> library).
    </p>
  </footer>
</body>
</html>
