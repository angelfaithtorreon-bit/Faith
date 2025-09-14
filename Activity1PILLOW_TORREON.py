from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

background = Image.new(mode="RGBA", size=(940, 788), color=(255, 192, 203, 255))  # Pink background
background = background.filter(ImageFilter.GaussianBlur(radius=10))  # Blur the background

trophy = Image.new(mode="RGBA", size=(940, 788), color=(255, 192, 203, 255))  
draw = ImageDraw.Draw(trophy)

title_font = ImageFont.truetype("FONTS/LCALLIG.ttf", 50)  
body_font = ImageFont.truetype("FONTS/CENSCBK.ttf", 42)


def vertical_gradient(draw, box, top_color, bottom_color):
    x0, y0, x1, y1 = box
    height = y1 - y0
    for i in range(height):
        
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * (i / height))
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * (i / height))
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * (i / height))
        draw.line([(x0, y0 + i), (x1, y0 + i)], fill=(r, g, b, 255))

def star_points(center, radius):
    cx, cy = center
    points = []
    for i in range(10):  
        angle = i * 36  
        rad = radius if i % 2 == 0 else radius / 2
        x = cx + rad * math.cos(math.radians(angle - 90))
        y = cy + rad * math.sin(math.radians(angle - 90))
        points.append((x, y))
    return points


GOLD_LIGHT = (255, 230, 120)  
BLACK = (200, 140, 20)   


star_center = (470, 380)
star_radius = 250


draw.polygon(star_points(star_center, star_radius), fill=GOLD_LIGHT, outline="SILVER")


draw.polygon(star_points(star_center, star_radius * 0.9), fill= BLACK)
connector_points = [
    (430, 530),  
    (510, 530),  
    (560, 580),  
    (380, 580),  
]

draw.polygon(connector_points, fill=GOLD_LIGHT, outline="white")

draw.rectangle([(350, 580), (590, 640)], fill="black")

plate_box = (370, 600, 570, 630)
vertical_gradient(draw, plate_box, (255, 220, 100), (200, 120, 10))
draw.rectangle(plate_box, outline="white", width=2)


text_top = "Most Enthusiastic Team"
bbox_top = draw.textbbox((0, 0), text_top, font=title_font)
w, h = bbox_top[2] - bbox_top[0], bbox_top[3] - bbox_top[1]
draw.text(((940 - w) / 2, 60), text_top, fill="black", font=title_font)


text_bottom = "COLLEGE OF COMPUTING AND\nINFORMATION SCIENCES"
bbox_bottom = draw.multiline_textbbox((0, 0), text_bottom, font=body_font, align="center")
bw, bh = bbox_bottom[2] - bbox_bottom[0], bbox_bottom[3] - bbox_bottom[1]
draw.multiline_text(((940 - bw) / 2, 660), text_bottom, fill="white", font=body_font, align="center")

final_image = Image.alpha_composite(background, trophy)

trophy.save("CSELEC3_3B_TorreonAngelFaith_Activity1.png")
trophy.show()