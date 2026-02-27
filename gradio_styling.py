import gradio as gr

# ── Kush Audio Inspired CSS ────────────────────────────────────
KUSH_CSS = """
.gradio-container { 
    background-color: #0d0d0d !important; 
    color: #e0e0e0 !important;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}
#chatbot { 
    background-color: #141414 !important; 
    border: 1px solid #2a2a2a !important;
    border-radius: 8px !important;
}
.message.user { 
    background-color: #1e1e1e !important; 
    border: 1px solid #333 !important;
}
.message.bot { 
    background-color: #141414 !important; 
    border-left: 3px solid #d4af37 !important;
}
#textbox textarea { 
    background-color: #1a1a1a !important; 
    color: #ffd700 !important; 
    border: 1px solid #333 !important;
}
footer { display: none !important; }
#main-title { 
    color: #d4af37; 
    text-transform: uppercase; 
    letter-spacing: 4px;
    font-weight: 300;
    margin-top: 40px;
    margin-bottom: 40px;
}
"""

def create_kush_header():
    """Returns the HTML component for the 'Ask My Thesis' header."""
    return gr.HTML("""
        <div style="text-align: center;">
            <h1 id="main-title">Ask My Thesis</h1>
        </div>
    """)