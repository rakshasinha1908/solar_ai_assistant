
---

## 🔆 Solar Industry AI Assistant

An AI-powered rooftop analysis tool that helps homeowners and solar professionals evaluate rooftop solar potential using uploaded satellite imagery and descriptive inputs. Built using Streamlit and OpenRouter (GPT-3.5).

---

## 🌞 Project Overview

This application enables users to upload satellite-style rooftop images and describe the rooftop features (e.g., size, sunlight exposure, obstructions). It then uses a language model to generate:

- Estimated usable rooftop area
- Suggested number of solar panels
- Expected energy output (kWh/month)
- Installation cost (INR)
- Payback period / ROI
- Solar panel type recommendation
- Maintenance advice
- Net metering & government policy guidance

---

## 📸 Why Descriptions Instead of Image Processing?

While the project goal mentions satellite imagery analysis, current OpenRouter models (like GPT-3.5 Turbo) **do not support direct image input or computer vision**.

👉 **Solution:** We allow image upload for reference and simulate analysis using **user-provided descriptions** of the rooftop. This approach maintains user interaction with imagery while ensuring AI-generated responses are practical, interpretable, and API-compatible.

---

## 🧠 AI Prompt Sample

```text
You are an expert solar engineer. Given the rooftop details below, provide:

1. Estimated usable area
2. Suggested number of panels
3. Energy output
4. Installation cost
5. ROI calculation
6. Solar panel type (mono/poly)
7. Maintenance advice
8. Government incentives/net metering (India)
9. Confidence score & assumptions

Rooftop Description:
Flat concrete rooftop, 100 sq.m, Delhi, 6 hours sunlight/day, minor shade from water tank.
````

---

## 🚀 Features

* 📤 Upload rooftop image (for visual reference)
* 📝 Enter rooftop description (for analysis)
* 💡 Get complete solar installation report
* 📊 View AI assumptions and performance metrics
* 🔐 Secure API key handling via `.env`

---

## 🛠️ How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/solar-ai-assistant
cd solar-ai-assistant
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create `.env` file** with your OpenRouter key:

```
OPENROUTER_API_KEY=your_actual_key_here
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🧪 Sample Output

📷 `sample_outputs/rooftop_sample.jpg`
📄 `sample_outputs/rooftop_sample_output.txt`

Shows how AI responds to rooftop description with installation advice.

---

## 📈 How ROI is Calculated

```
ROI = Installation Cost ÷ Estimated Monthly Savings
```

Example: ₹1,00,000 cost ÷ ₹1,500/month = \~66 months (\~5.5 years payback)

---

## ⚡ Performance Metrics

| Metric             | Value                |
| ------------------ | -------------------- |
| Avg. Response Time | 3–5 seconds          |
| Max Upload Size    | 5MB                  |
| API Used           | OpenRouter (GPT-3.5) |
| Cost               | Free (under trial)   |
| Uptime (local)     | 100%                 |

---

## 🧠 Future Improvements

* 🎯 Use real vision models (e.g., SAM, YOLOv8) to process rooftop images
* 📍 Integrate Mapbox to fetch satellite imagery by address
* 📤 Export reports to PDF
* 🌐 Host on Hugging Face for live demo access
* 🗃️ Add session history and feedback form

---

## 👩‍💻 Developer

**Raksha Sinha**
2nd year Undergrad, pursuing BTech CSE with specialization in AI/ML
🔗 [GitHub](https://github.com/rakshasinha1908)

---

## 🧠 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [OpenRouter](https://openrouter.ai)
* [Hugging Face Spaces](https://huggingface.co/spaces)


