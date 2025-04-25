# 🧠 Agent Creation API (FastAPI)

This FastAPI project exposes a unified endpoint `/create-agent` to create AI voice agents using either **Vapi** or **Retell** APIs. The goal is to provide a simple interface where the user only specifies the `provider`, and the backend handles the rest.

---

## 🔧 Tech Stack

- **FastAPI** – Python web framework for building APIs
- **Pydantic** – For request validation
- **Requests** – For making HTTP calls to external APIs
- **Python-dotenv** – To load environment variables from `.env`

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/agent-creator-api.git
cd agent-creator-api
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
VAPI_API_KEY=your_vapi_api_key_here
RETELL_API_KEY=your_retell_api_key_here
```

---

## 🚀 Running the API

```bash
uvicorn main:app --reload
```

Once the server is up, open [http://localhost:8000/docs](http://localhost:8000/docs) to explore the Swagger UI.

---

## 🧪 API Usage

### **POST** `/create-agent`

#### Request Body

```json
{
  "provider": "vapi" | "retell",
  "name": "Optional Custom Name"
}
```

- `provider`: `"vapi"` or `"retell"` — determines which API to use.
- `name`: Optional name for the agent (currently not used in the backend request).

#### Example cURL

```bash
curl -X POST http://localhost:8000/create-agent \
-H "Content-Type: application/json" \
-d '{"provider": "retell", "name": "My Retell Agent"}'
```


## 💡 Design Decision

- The `model`, `voice_id`, and other required parameters are **internally hardcoded** based on the selected provider.
- This ensures the external API stays clean and user-friendly with minimal input.

---

## 🛠 Future Improvements

- Support dynamic model/voice_id inputs
- Store created agents in a database
- Add user authentication
- Logging and rate limiting

---

## 🧑‍💻 Author

Made with ❤️ by Ankur Pal  
[LinkedIn](https://www.linkedin.com/in/ankur-pal) • [GitHub](https://github.com/ItsAnkurPal)

---
