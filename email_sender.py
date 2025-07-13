import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

# For full HTML rendering
import streamlit.components.v1 as components

# Configuration (use st.secrets in production)
YOUR_EMAIL = "technestintern.intern@gmail.com"
YOUR_PASSWORD = "mogkdkvyjgwqeaeq"

# Streamlit UI
st.set_page_config(page_title="TechNest Auto Mail Tool", layout="centered")
st.markdown("## 💌 TechNest Webinar - Auto Mail Sender")

receiver_email = st.text_input("Enter Intern's Email")
send_button = st.button("Send Email")

# Email subject
subject = "🎉📢 Don’t Miss Our Free Webinar + Certificate | Support Us on LinkedIn!"
st.markdown(f"**Email Subject:** {subject}")

# Email HTML Body
html_body = """
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f7f9fc; padding: 20px; color: #333;">
    <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 10px; padding: 25px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">

      <p style="font-size: 16px;">Dear,</p>
      <p style="font-size: 16px;">Hope you’re doing well!</p>

      <p style="font-size: 17px;">🚨 <strong>You're invited!</strong> Join us for an exclusive <strong>free live webinar</strong> by <strong>TechNest Intern</strong>:</p>

      <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

      <h3 style="color: #2c3e50;">🧠 “  Mahabharat of Prompts: Aligning Truth, Bias, and Outcomes in Generative AI  🤖”</h3>
      <ul style="padding-left: 20px;">
      <li><strong>📅 Date:</strong>  15th July , Tuesday </li>
      <li><strong>⏰ Time:</strong> 8:00 PM – 9:00 PM IST</li>
      <li><strong>🎓 Certificate:</strong> Participation certificate for all attendees</li>
      <li><strong>📍 Mode:</strong> Online (Google Meet)</li>
      <p>✅ Learn practical prompt tips for ChatGPT, Bard, Gemini & more!<br>
      ✅ Mentored by expert Training Coach – <strong>Sagar Chavan</strong></p>

      <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

      <h3 style="color: #2c3e50;">🔗 Register Now:</h3>
      <p style="margin-bottom: 5px;"><strong>📄 Offer Letter:</strong></p>
      👉 <a href="https://forms.gle/pDBpwyQxuhbdVtcQ9" target="_blank" style="color: #007bff; text-decoration: none;">Click here to Register</a>

      <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 20px;">

      <h3 style="color: #2c3e50;">💬 Want to Support Us?</h3>
      <p>We shared this on LinkedIn to reach more learners 🚀</p>
      👉 <a href="https://www.linkedin.com/posts/technestintern_interested-technestintern-projectbasedlearning-activity-7348928805085851649-KIq7?utm_source=share&utm_medium=member_desktop&rcm=ACoAADyrA8ABDjvqLEXOyKCCPROvoy4zopaDM3M" target="_blank" style="color: #007bff; text-decoration: none;">Visit the LinkedIn Post</a>

      <p>If you believe in TechNest Intern and our mission:</p>
      <ul style="padding-left: 20px;">
        <li>✅ Like the post</li>
        <li>✅ Comment with <strong>#cfbr</strong> (to boost visibility)</li>
        <li>✅ Tag a friend who would love to attend</li>
      </ul>

      <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

      <p>Thanks for being part of our learning community.<br>
      Let’s grow and build opportunities — <strong>together 💙</strong></p>

      <p style="margin-top: 20px;">
        Best regards,<br>
        <strong>TechNest Intern</strong><br>
      🔗<a href="https://www.linkedin.com/company/technestintern/about/" target="_blank" style="color: #007bff;">Follow on LinkedIn</a>
      </p>

      <img src="https://i.ibb.co/G4xpC90w/logo.png" alt="TechNest Logo" width="140" style="margin-top: 20px;">

    </div>
  </body>
</html>

"""



# Email Sending Logic
if send_button and receiver_email:
    email_list = [email.strip() for email in receiver_email.split(",") if email.strip()]

    success_list = []
    fail_list = []

    for email in email_list:
        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = YOUR_EMAIL
            msg["To"] = email

            msg.attach(MIMEText(html_body, "html"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(YOUR_EMAIL, YOUR_PASSWORD)
                server.sendmail(YOUR_EMAIL, email, msg.as_string())

            success_list.append(email)
        except Exception as e:
            fail_list.append((email, str(e)))

    if success_list:
        st.success("✅ Email sent to:\n" + ", ".join(success_list))
    if fail_list:
        st.error("❌ Failed to send to:")
        for email, err in fail_list:
            st.error(f"{email} ➜ {err}")

# Full HTML Preview
st.markdown("### 📨 Email Preview")
components.html(html_body, height=2000,)
