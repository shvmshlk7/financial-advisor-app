from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Financial Advisor Project - Analysis Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

def create_report():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '1. Project Overview', 0, 1)
    
    pdf.set_font('Arial', '', 12)
    overview = (
        "The Financial Advisor project is a full-stack AI-powered financial advisory platform. "
        "It provides users with real-time stock metrics, financial news, portfolio management, "
        "and an AI-driven chatbot for financial queries. The platform uses a React-based Next.js "
        "frontend and a Python-based Flask backend."
    )
    pdf.multi_cell(0, 10, overview)
    pdf.ln(5)
    
    # Architecture
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '2. Architecture & Tech Stack', 0, 1)
    
    pdf.set_font('Arial', '', 12)
    tech_stack = (
        "- Frontend: Next.js, React, Tailwind CSS, Recharts, Chart.js, Framer Motion.\n"
        "- Backend: Python, Flask, Flask-CORS, Flask-JWT-Extended.\n"
        "- Database: MongoDB (via PyMongo).\n"
        "- External APIs: yfinance (Market Data), Alpha Vantage, Google Generative AI (Gemini), News APIs."
    )
    pdf.multi_cell(0, 10, tech_stack)
    pdf.ln(5)
    
    # Key Features
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '3. Key Features', 0, 1)
    
    pdf.set_font('Arial', '', 12)
    features = (
        "1. User Authentication: Secure login and registration using JWT.\n"
        "2. Dashboard: A comprehensive view of market trends, global and Indian financial news.\n"
        "3. Stock Metrics: Live financial data analysis and visualization.\n"
        "4. Portfolio Management: Users can track and manage their investments.\n"
        "5. AI Chatbot: An integrated Gemini-powered assistant capable of answering financial questions."
    )
    pdf.multi_cell(0, 10, features)
    pdf.ln(5)
    
    # How to run
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '4. Running the Project', 0, 1)
    
    pdf.set_font('Arial', '', 12)
    run_instructions = (
        "Backend (Flask):\n"
        "1. Create a virtual environment and activate it.\n"
        "2. Install dependencies via `pip install -r backend/requirements.txt`.\n"
        "3. Add a `.env` file in the backend folder containing `MONGODB_URI`, `JWT_SECRET_KEY`, etc.\n"
        "4. Run the backend server using `python app.py` on port 5000.\n\n"
        "Frontend (Next.js):\n"
        "1. Navigate to the root directory.\n"
        "2. Install Node dependencies with `npm install`.\n"
        "3. Start the development server using `npm run dev` on port 3000."
    )
    pdf.multi_cell(0, 10, run_instructions)
    
    pdf.output('Financial_Advisor_Report.pdf')

if __name__ == '__main__':
    create_report()
