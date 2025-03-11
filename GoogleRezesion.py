import webbrowser
import os
import random
import base64

def get_random_color():
    colors = ["#F2C744", "#594919", "#3357FF", "#0D2340"]
    return random.choice(colors)


def get_random_profile_picture_base64():
    img_paths = [
        "Profile_picture/eleinstein_Kopf.png",
        "Profile_picture/El_Tony_Kopf_v2.png",
    ]
    img_path = random.choice(img_paths)
    with open(img_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode("utf-8")
        # Determine MIME type based on extension
        mime_type = "image/png" if img_path.endswith(".png") else "image/jpeg"
        return f"data:{mime_type};base64,{img_data}"

def calculate_star_distribution(comments):
    star_counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for comment in comments:
        star = int(comment["stars"])  # Round down to nearest integer
        star_counts[star] += 1
    total_reviews = len(comments)
    star_percentages = {star: (count / total_reviews * 100) if total_reviews > 0 else 0 for star, count in star_counts.items()}
    return star_percentages

def insert_average_rezession(rezession_stars, anzahl_rezessionen, comments):
    round_rezession_stars = round(rezession_stars * 2) / 2
    star_percentages = calculate_star_distribution(comments)
    
    # Create the bar chart for star distribution
    bar_chart = ""
    for star in range(5, 0, -1):
        percentage = star_percentages[star]
        bar_chart += f"""
        <div class="star-row">
            <span class="star-label">{star}</span>
            <div class="star-bar-background">
                <div class="star-bar-fill" style="width: {percentage}%; background: linear-gradient(90deg, #F4B400, #FFC107);"></div>
            </div>
        </div>
        """
    
    html_content = f"""
    <div class="summary-container">
        <div class="summary-header">EBL-Rezensionen im Überblick</div>
        <div class="summary-content">
            <div class="average-rating">
                <span class="average-score">{round_rezession_stars}</span>
                <div class="stars-average">
                    {'★' * int(round_rezession_stars)}{'<span class="half-star"></span>' if round_rezession_stars % 1 >= 0.5 else ''}{'☆' * (5 - int(round_rezession_stars) - (1 if round_rezession_stars % 1 >= 0.5 else 0))}
                </div>
            </div>
            <div class="star-distribution">
                {bar_chart}
            </div>
        </div>
        <div class="total-reviews">{anzahl_rezessionen} Rezensionen</div>
    </div>
    """
    return html_content

def insert_profile_head():
    img_data_url = get_random_profile_picture_base64()
    return f'<div class="profile-pic-head" style="background-image: url(\'{img_data_url}\')"></div>'

def insert_profile_color(letter):
    color = get_random_color()
    return f'<div class="profile-pic-color" style="background-color: {color}">{letter}</div>'

def insert_Google_Rezession(user: str, stars, text, head=False):
    if head:
        html_content = f"""
        <div class="review-container">
            <div class="user-info">
                {insert_profile_head()}
                <div class="username"><strong>{user}</strong></div>
            </div>
            <div class="points" style="display: inline;">{stars}</div>
            <div class="stars" style="display: inline;">
                {'★' * int(stars)}{'<span class="half-star"></span>' if stars % 1 == 0.5 else ''}{'☆' * (5 - int(stars) - (1 if stars % 1 == 0.5 else 0))}
            </div>
            <div class="text">
                {text}
            </div>
        </div>
        """
    else:
        initial = user[0].upper()
        html_content = f"""
        <div class="review-container">
            <div class="user-info">
                {insert_profile_color(initial)}
                <div class="username"><strong>{user}</strong></div>
            </div>
            <div class="points" style="display: inline;">{stars}</div>
            <div class="stars" style="display: inline;">
                {'★' * int(stars)}{'<span class="half-star"></span>' if stars % 1 == 0.5 else ''}{'☆' * (5 - int(stars) - (1 if stars % 1 == 0.5 else 0))}
            </div>
            <div class="text">
                {text}
            </div>
        </div>
        """
    return html_content

def create_comment_list(comments):
    html_content = ""
    for comment in comments:
        html_content += insert_Google_Rezession(comment["user"], comment["stars"], comment["text"], head=comment["user"] == "Anonym")
    return html_content

comments = [
    {"user": "Anonym", "stars": 2, "text": "Die Intention dahinter ist sinvoll, die Ausführung absolut undurchdacht. Das Ganze im Abschlussjahr zu beginnen ist rücksichtslos. Die Lehrer machen eigentlich nichts und werden trotzdem bezahlt.🙂"},
    {"user": "Anonym", "stars": 2, "text": "Hatte nach einer Benutzung genug und verwende es nun eigentlich nicht mehr. Da ein Umtausch ausgeschlossen ist, ist es einfach nur noch unnötig. Habe allerdings einen Weg gefunden es anderweitig zu nutzen, darum 2 Sterne. Kann es trotzdem nicht weiter empfehlen."},
    {"user": "Hauptsach Bestande", "stars": 2, "text": "Die Bildung wird gegen die Wand gefahren aber die Träume sind dafür umso schöner."},
    {"user": "Anonym", "stars": 1, "text": 'EBL ist genau dann gut, wenn es das Fach "Freizeit" in der Schule geben würde.'},
    {"user": "Anonym", "stars": 2, "text": 'EBL = einfach besser liegenbleiben'},
    
    {"user": "EBLover", "stars": 3, "text": 'eigentlich super, man kann ausschlafen, sport machen, chillen oder *E*ifach *B*izzli *L*iggebliibe, deshalb rundum gute sache. einziges klitzekleines problem, das man bemängeln könnte ist der lernerfolg, der arg beeinträchtigt wird aber das ist ja nebensächlich.'},
    {"user": "Albert Rüchig", "stars": 4, "text": "Ich finde es schön, dass unser Schulsystem sich so fest um den Schlaf der Schüler kümmert und darum das EBL eingeführt hat 👍"},
    {"user": "Anonym", "stars": 5, "text": 'Man kann es machen wann man will und wie genau man will.'},
    {"user": "Dr. Schlaumeier", "stars": 4, "text": "Endlich wird keine Zeit vergeudet in Sitzbänken zu verfaulen."},
    {"user": "Albert Zweistein", "stars": 5, "text": 'Liebe alles daran bis auf den Abend vor der Prüfung, wenn man sich 5 Wochen Stoff in 1er Stunde SELBER zusammendichten muss, bin bald Goethe!'},
]



rezession_stars = 2.96
anzahl_rezessionen = 78


html_content = f"""
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Review</title>
    <style>
        @page {{
            size: A4;
            margin: 15mm; /* Reduced from 20mm for more content space */
        }}
        body {{
            font-family: 'Roboto', Arial, sans-serif;
            background: #ffffff; /* White background outside A4 */
            margin: 0;
        }}
        .a4-page {{
            background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
            width: 764px; /* 794px - 3 * 10px padding */
            height: 1093px; /* 1123px - 2 * 15px margins, fixed height */
            padding: 15px; /* Internal padding */
            box-sizing: border-box;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        .page-container {{
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            gap: 15px; /* Reduced gap for more content width */
            height: 100%;
            width: 100%;
        }}
        .column {{
            width: 387px; /* Adjusted to fit within 774px with gap */
            display: flex;
            flex-direction: column;
        }}
        .review-container {{
            background: linear-gradient(145deg, #ffffff, #f0f4f8);
            border-radius: 6px;
            padding: 8px; /* Reduced padding */
            width: 339px;
            margin-bottom: 8px; /* Reduced margin */
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-container {{
            background: linear-gradient(145deg, #ffffff, #f0f4f8);
            border-radius: 10px;
            padding: 8px; /* Reduced padding */
            width: 339px; /* Adjusted to fit column */
            margin-bottom: 15px; /* Reduced margin */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .summary-header {{
            font-size: 14px; /* Slightly smaller */
            font-weight: bold;
            margin-bottom: 8px;
            color: #202124;
        }}
        .summary-content {{
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }}
        .average-rating {{
            text-align: center;
            margin-right: 10px;
        }}
        .average-score {{
            font-size: 32px; /* Slightly smaller */
            font-weight: bold;
            color: #202124;
        }}
        .stars-average {{
            color: #F4B400;
            font-size: 12px; /* Smaller */
        }}
        .star-distribution {{
            flex-grow: 1;
        }}
        .star-row {{
            display: flex;
            align-items: center;
            margin-bottom: 2px; /* Tighter spacing */
        }}
        .star-label {{
            width: 16px;
            font-size: 10px; /* Smaller */
            color: #5f6368;
            margin-right: 6px;
        }}
        .star-bar-background {{
            flex-grow: 1;
            height: 5px; /* Thinner bars */
            background: linear-gradient(90deg, #dadce0, #e8ecef);
            border-radius: 2px;
            overflow: hidden;
        }}
        .star-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, #F4B400, #FFC107);
            border-radius: 2px;
        }}
        .total-reviews {{
            font-size: 10px; /* Smaller */
            color: #5f6368;
            margin-bottom: 8px;
        }}
        
        .stars {{
            color: #F4B400;
            font-size: 10px; /* Smaller */
        }}
        .text {{
            margin-top: 4px;
            font-size: 10px; /* Smaller */
            color: #202124;
            line-height: 1.2; /* Tighter line height */
            word-wrap: break-word;
        }}
        .half-star {{
            position: relative;
            display: inline-block;
        }}
        .half-star:before {{
            content: "★";
            position: absolute;
            width: 50%;
            overflow: hidden;
            color: #F4B400;
        }}
        .half-star:after {{
            content: "☆";
            color: #dadce0;
        }}
        .profile-pic-color, .profile-pic-head {{
            width: 20px; /* Smaller */
            height: 20px;
            border-radius: 50%;
            margin-right: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 10px; /* Smaller */
            font-weight: bold;
            background-size: cover;
            box-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }}
        .user-info {{
            display: flex;
            align-items: center;
            margin-bottom: 2px; /* Tighter spacing */
        }}
        .username {{
            font-size: 10px; /* Smaller */
            font-weight: 500;
            color: #202124;
        }}
        .points {{
            font-size: 10px; /* Smaller */
            margin-right: 3px;
            color: #5f6368;
        }}
        @media print {{
            body {{
                padding: 0;
            }}
            .a4-page {{
                box-shadow: none; /* Remove shadow for print */
                width: 100%;
                height: 100%;
                padding: 15mm; /* Match @page margin */
            }}
        }}
    </style>
</head>
<body>
    <div class="a4-page">
        <div class="page-container">
            <div class="column">
                {insert_average_rezession(rezession_stars, anzahl_rezessionen, comments)}
                {''.join([create_comment_list(comments[i::2]) for i in range(0, 2, 2)])}
            </div>
            <div class="column">
                {''.join([create_comment_list(comments[i::2]) for i in range(1, 2, 2)])}
            </div>
        </div>
    </div>
</body>
</html>
"""

# Save and open the HTML file
html_file_path = os.path.abspath(r'GoogleRezession/review.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
webbrowser.open('file://' + html_file_path)