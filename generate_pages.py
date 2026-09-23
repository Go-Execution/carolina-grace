import os
import random

pages = [
    ("home-care.html", "Home Care", "Comprehensive in-home care services designed to help your loved ones live comfortably and safely.", "images/hero.jpg"),
    ("community-care.html", "Community Care", "Engaging community care programs to ensure social interaction and active lifestyles.", "images/companionship.jpg"),
    ("dementia-support.html", "Dementia Support", "Specialized, compassionate care for individuals living with Dementia.", "images/hero.jpg"),
    ("alzheimers-support.html", "Alzheimer's Support", "Dedicated Alzheimer's support to provide peace of mind for families and comfort for patients.", "images/companionship.jpg"),
    ("24-hour-care.html", "24-Hour Care", "Round-the-clock care and monitoring to guarantee safety and assistance at any time of day.", "images/hero.jpg"),
    ("personal-care.html", "Personal Care", "Respectful assistance with daily personal hygiene, grooming, and dressing.", "images/daily_living.jpg"),
    ("companion-care.html", "Companion Care", "Meaningful companionship to prevent isolation and encourage mental engagement.", "images/companionship.jpg"),
    ("overnight-care.html", "Overnight Care", "Attentive overnight support so families can rest easy knowing their loved ones are safe.", "images/hero.jpg"),
    ("respite-care.html", "Respite Care", "Temporary relief for primary caregivers, ensuring continuous, high-quality support.", "images/companionship.jpg"),
    ("hygiene-support.html", "Hygiene Support", "Discreet and dignified support with bathing, toileting, and general hygiene needs.", "images/daily_living.jpg"),
    ("about-us.html", "About Us", "Learn more about Carolina Grace Home Care, our mission, and our dedicated team of caregivers.", "images/hero.jpg"),
    ("careers.html", "Careers", "Join our compassionate team. We are always looking for dedicated caregivers to make a difference.", "images/hero.jpg"),
    ("contact.html", "Contact Us", "Get in touch with us today to schedule a free in-home assessment and discover how we can help.", "images/companionship.jpg")
]

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

header_end = content.find("</header>") + 9
header = content[:header_end]

footer_start = content.find("<!-- Areas Served Section -->")
footer = content[footer_start:]

for filename, title, desc, img in pages:
    page_html = header + f"""

    <!-- Page Hero -->
    <section class="page-hero" style="background-color: var(--primary-blue); color: white; padding: 100px 0; text-align: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 20px; font-family: var(--font-heading); color: white;">{title}</h1>
            <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; color: #e0f2f1;">{desc}</p>
        </div>
    </section>

    <!-- Overview Section -->
    <section class="section about">
        <div class="container about-container" style="align-items: center;">
            <div class="about-text">
                <h4 class="subtitle">Overview</h4>
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Exceptional {title} Services</h2>
                <p style="margin-bottom: 20px;">At Carolina Grace Home Care, we understand that every individual requires a unique approach to care. Our <strong>{title}</strong> services are designed with compassion, dignity, and respect at their core.</p>
                <p style="margin-bottom: 30px;">{desc} We work closely with families to develop a customized care plan that fits seamlessly into your daily life, ensuring safety, comfort, and peace of mind.</p>
                <a href="index.html#contact" class="btn btn-primary">Schedule an Assessment</a>
            </div>
            <div class="about-features" style="display: block;">
                <img src="{img}" alt="{title}" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            </div>
        </div>
    </section>

    <!-- Key Benefits Section -->
    <section class="section bg-light text-center">
        <div class="container">
            <h4 class="subtitle">Why Choose Us</h4>
            <h2 style="margin-bottom: 50px;">The Carolina Grace Difference</h2>
            
            <div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                <div class="service-card" style="padding: 40px 20px;">
                    <div style="font-size: 3rem; color: var(--primary-green); margin-bottom: 15px;">♥</div>
                    <h3>Compassionate Staff</h3>
                    <p>Our caregivers are thoroughly vetted, highly trained, and deeply passionate about helping others.</p>
                </div>
                <div class="service-card" style="padding: 40px 20px;">
                    <div style="font-size: 3rem; color: var(--primary-green); margin-bottom: 15px;">✓</div>
                    <h3>Customized Plans</h3>
                    <p>We don't believe in one-size-fits-all. Every care plan is tailored to your specific needs.</p>
                </div>
                <div class="service-card" style="padding: 40px 20px;">
                    <div style="font-size: 3rem; color: var(--primary-green); margin-bottom: 15px;">⏱</div>
                    <h3>Flexible Scheduling</h3>
                    <p>Whether you need a few hours a week or 24/7 care, we adapt to your schedule.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="section" style="background-color: var(--primary-green); color: white; text-align: center;">
        <div class="container">
            <h2 style="font-size: 2.5rem; margin-bottom: 20px; color: white;">Ready to get started with {title}?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 30px; max-width: 600px; margin-left: auto; margin-right: auto; color: white;">Our team is standing by to answer your questions and set up a free in-home consultation.</p>
            <a href="index.html#contact" class="btn btn-outline-white">Contact Us Today</a>
        </div>
    </section>

""" + footer
    
    page_html = page_html.replace("<title>Carolina Grace Home Care | Charlotte, NC</title>", f"<title>{title} | Carolina Grace Home Care</title>")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_html)

print("Pages regenerated successfully.")
