import os

pages = [
    ("home-care.html", "Home Care", "Comprehensive in-home care services designed to help your loved ones live comfortably and safely."),
    ("community-care.html", "Community Care", "Engaging community care programs to ensure social interaction and active lifestyles."),
    ("dementia-support.html", "Dementia Support", "Specialized, compassionate care for individuals living with Dementia."),
    ("alzheimers-support.html", "Alzheimer's Support", "Dedicated Alzheimer's support to provide peace of mind for families and comfort for patients."),
    ("24-hour-care.html", "24-Hour Care", "Round-the-clock care and monitoring to guarantee safety and assistance at any time of day."),
    ("personal-care.html", "Personal Care", "Respectful assistance with daily personal hygiene, grooming, and dressing."),
    ("companion-care.html", "Companion Care", "Meaningful companionship to prevent isolation and encourage mental engagement."),
    ("overnight-care.html", "Overnight Care", "Attentive overnight support so families can rest easy knowing their loved ones are safe."),
    ("respite-care.html", "Respite Care", "Temporary relief for primary caregivers, ensuring continuous, high-quality support."),
    ("hygiene-support.html", "Hygiene Support", "Discreet and dignified support with bathing, toileting, and general hygiene needs."),
    ("about-us.html", "About Us", "Learn more about Carolina Grace Home Care, our mission, and our dedicated team of caregivers."),
    ("careers.html", "Careers", "Join our compassionate team. We are always looking for dedicated caregivers to make a difference."),
    ("contact.html", "Contact Us", "Get in touch with us today to schedule a free in-home assessment and discover how we can help.")
]

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract header (up to </header>)
header_end = content.find("</header>") + 9
header = content[:header_end]

# Extract footer (from <!-- Areas Served Section --> onwards)
footer_start = content.find("<!-- Areas Served Section -->")
footer = content[footer_start:]

# Generate pages
for filename, title, desc in pages:
    page_html = header + f"""

    <section class="section bg-light" style="min-height: 50vh; display: flex; align-items: center; justify-content: center; text-align: center;">
        <div class="container">
            <h1 style="color: var(--primary-blue); font-size: 3rem; margin-bottom: 20px;">{title}</h1>
            <p style="font-size: 1.2rem; color: #555; max-width: 700px; margin: 0 auto;">{desc}</p>
            <br><br>
            <a href="index.html#contact" class="btn btn-primary">Request Care</a>
        </div>
    </section>

""" + footer
    
    # Update title tag
    page_html = page_html.replace("<title>Carolina Grace Home Care | Charlotte, NC</title>", f"<title>{title} | Carolina Grace Home Care</title>")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_html)

print("Pages generated successfully.")
