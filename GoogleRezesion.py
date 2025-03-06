import webbrowser
import os
import random
def get_random_color():
    colors = ["#F2C744", "#594919", "#3357FF", "#0D2340"]
    return random.choice(colors)

def get_random_profile_picture():
    img_paths = [
                 "Profile_picture/eleinstein_Kopf.png",]
    return random.choice(img_paths)

def insert_average_rezession(rezession_stars, anzahl_rezessionen):
    round_rezession_stars = round(rezession_stars * 2) / 2
    html_content = f"""
    <div class="review-container">
        {rezession_stars} 
        <div class="stars" style="display: inline;">
            {'★' * int(round_rezession_stars)}{'<span class="half-star"></span>' if round_rezession_stars % 1 >= 0.5 else ''}{'☆' * (5 - int(round_rezession_stars) - (1 if round_rezession_stars % 1 == 0.5 else 0))}
        </div>
        ({anzahl_rezessionen})
    </div>
    """
    return html_content

def insert_profile_head():
    img_path = get_random_profile_picture()
    return f'<div class="profile-pic_head" style="background-image: url(\'{img_path}\')"></div>'

def insert_profile_color(letter):
    color = get_random_color()
    return f'<div class="profile-pic_color" style="background-color: {color}">{letter}</div>'

def insert_Google_Rezession(user:str, stars, text, head=False):
    if head:
        html_content = f"""
        <div class="review-container">
            <div class="user-info">
                {insert_profile_head()}
                <div><strong>{user}</strong></div>
            </div>
            {stars}
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
                <div><strong>{user}</strong></div>
            </div>
            {stars}
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
        {"user": "Anonym", "stars": 5, "text": 'This is a great python code that quickly generates a Google review page. If you are working with chrome, just click F12 and select the wanted element. '},
        {"user": "name", "stars": 4.3, "text": 'Click on the tree dots right next to the div container and press on "capture node screenshot". This will save the div container as a png file.'},

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
        .review-container {{
            font-family: Arial, sans-serif;
            border: 1px solid #ccc;
            padding: 20px;
            width: 350px;
            margin: 0 auto;
        }}
        .stars {{
            color: gold;
            font-size: 20px;
        }}
        .text {{
            margin-top: 10px;

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
        }}
        .half-star:after {{
            content: "☆";
        }}
        .profile-pic_color {{
            width: 35px;
            height: 35px;
            border-radius: 50%;
            margin-right: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            background-size: cover;
        }}
        .profile-pic_head {{
            width: 35px;
            height: 35px;
            border-radius: 50%;
            margin-right: 20px;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-size: cover;
        }}
        .user-info {{
            display: flex;
            align-items: center;
        }}
    </style>
</head>
<body>
    {insert_average_rezession(rezession_stars, anzahl_rezessionen)}
    {create_comment_list(comments)}
</body>
</html>
"""




# Save the HTML content to a file
html_file_path = os.path.abspath(r'GoogleRezession\review.html')
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open('file://' + html_file_path)



