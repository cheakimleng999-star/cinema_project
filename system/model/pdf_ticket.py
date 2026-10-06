from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code128
import math
import json
import random
import string

def mainss():
    with open('system/database/total_payment.json', 'r') as f:
        data = json.load(f)
        for i in data:
            m = i['name_movie']
            n = i["total"]

    with open('system/database/movie_data.json', 'r') as f:
        data = json.load(f)
        for i in data:
            h = i['time_start']
            ss = str(i['ID'])

    with open('system/database/client.json', 'r') as f:
        data = json.load(f)
    users = {}
    for i in data:
        ds = i["time"]
        ticket_number = ds
    for item in data:

        user = item["user"]
        seat = item["seat"]

        if user not in users:
            users[user] = []

        users[user].append(seat)

    for user, seats in users.items():
        total_payment = n
        hall = ss
        date = h
        theater = m
        seat = ", ".join(map(str, seats))

    WIDTH = 190 * mm
    HEIGHT = 100 * mm

    filename = "cinema_ticket_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".pdf"
    pdf = canvas.Canvas(filename, pagesize=(WIDTH, HEIGHT))

    RED = colors.HexColor("#D71920")
    CREAM = colors.HexColor("#F5F0E5")
    GRAY = colors.HexColor("#E8E8E8")
    DARK = colors.HexColor("#222222")


    pdf.setFillColor(GRAY)
    pdf.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)



    x = 8 * mm
    y = 8 * mm

    ticket_width = WIDTH - 16 * mm
    ticket_height = HEIGHT - 16 * mm

    pdf.setFillColor(CREAM)
    pdf.roundRect(
        x,
        y,
        ticket_width,
        ticket_height,
        5 * mm,
        fill=1,
        stroke=0
    )

    top_height = 25 * mm

    pdf.setFillColor(RED)

    pdf.roundRect(
        x,
        y + ticket_height - top_height,
        ticket_width,
        top_height,
        5 * mm,
        fill=1,
        stroke=0
    )

    # Make bottom of red area straight
    pdf.rect(
        x,
        y + ticket_height - top_height,
        ticket_width,
        8 * mm,
        fill=1,
        stroke=0
    )

    side_width = 14 * mm

    pdf.setFillColor(RED)

    pdf.rect(
        x + ticket_width - side_width,
        y,
        side_width,
        ticket_height,
        fill=1,
        stroke=0
    )

    perforation_x = x + 48 * mm

    pdf.setStrokeColor(colors.HexColor("#999999"))
    pdf.setLineWidth(0.7)
    pdf.setDash(3, 3)

    pdf.line(
        perforation_x,
        y,
        perforation_x,
        y + ticket_height
    )

    pdf.setDash()

    def draw_star(pdf, cx, cy, outer_radius, inner_radius):
        points = []

        for i in range(10):

            angle = math.radians(90 + i * 36)

            if i % 2 == 0:
                radius = outer_radius
            else:
                radius = inner_radius

            px = cx + math.cos(angle) * radius
            py = cy + math.sin(angle) * radius

            points.append((px, py))

        path = pdf.beginPath()

        path.moveTo(points[0][0], points[0][1])

        for px, py in points[1:]:
            path.lineTo(px, py)

        path.close()

        pdf.drawPath(path, fill=1, stroke=0)

    pdf.setFillColor(colors.white)

    star_y = y + ticket_height - 12 * mm

    for i in range(5):

        star_x = x + 65 * mm + i * 18 * mm

        draw_star(
            pdf,
            star_x,
            star_y,
            5 * mm,
            2.2 * mm
        )

    pdf.setFillColor(colors.white)

    pdf.setFont("Helvetica-Bold", 10)

    pdf.drawString(
        x + 8 * mm,
        y + ticket_height - 9 * mm,
        "CINEMA"
    )

    pdf.drawString(
        x + 8 * mm,
        y + ticket_height - 17 * mm,
        "TICKET"
    )


    pdf.setFillColor(DARK)

    pdf.setFont("Helvetica-Bold", 9)

    pdf.drawString(
        x + 8 * mm,
        y + ticket_height - 33 * mm,
        ticket_number
    )

    barcode = code128.Code128(
        ticket_number,
        barHeight=12 * mm,
        barWidth=0.65
    )

    barcode.drawOn(
        pdf,
        x + 8 * mm,
        y + 36 * mm
    )

    pdf.setFillColor(DARK)

    pdf.setFont("Helvetica-Bold", 7)

    pdf.drawString(
        x + 20 * mm,
        y + 28 * mm,
        "time start:"
    )

    pdf.drawString(
        x + 20 * mm,
        y + 22 * mm,
        date
    )

    pdf.drawString(
        x + 20 * mm,
        y + 15 * mm,
        "MOVIE: " + theater
    )

    pdf.drawString(
        x + 20 * mm,
        y + 8 * mm,
        "seat: " + seat
    )


    def draw_camera(pdf, x, y):

        pdf.setFillColor(RED)

        # Camera body
        pdf.roundRect(
            x,
            y,
            15 * mm,
            10 * mm,
            1.5 * mm,
            fill=1,
            stroke=0
        )


        path = pdf.beginPath()

        path.moveTo(
            x + 15 * mm,
            y + 7 * mm
        )

        path.lineTo(
            x + 23 * mm,
            y + 11 * mm
        )

        path.lineTo(
            x + 23 * mm,
            y + 3 * mm
        )

        path.lineTo(
            x + 15 * mm,
            y + 6 * mm
        )

        path.close()

        pdf.drawPath(path, fill=1, stroke=0)


        pdf.circle(
            x + 4 * mm,
            y + 13 * mm,
            4 * mm,
            fill=1,
            stroke=0
        )

        # Reel 2
        pdf.circle(
            x + 12 * mm,
            y + 13 * mm,
            4 * mm,
            fill=1,
            stroke=0
        )

        # Tripod
        pdf.setStrokeColor(RED)
        pdf.setLineWidth(1.5)

        pdf.line(
            x + 8 * mm,
            y,
            x + 3 * mm,
            y - 9 * mm
        )

        pdf.line(
            x + 8 * mm,
            y,
            x + 13 * mm,
            y - 9 * mm
        )

        pdf.line(
            x + 8 * mm,
            y,
            x + 8 * mm,
            y - 9 * mm
        )


    draw_camera(
        pdf,
        x + 63 * mm,
        y + 38 * mm
    )

    pdf.setFillColor(RED)

    pdf.setFont("Helvetica-Bold", 22)

    pdf.drawString(
        x + 93 * mm,
        y + 55 * mm,
        "CINEMA"
    )

    pdf.drawString(
        x + 93 * mm,
        y + 43 * mm,
        "TICKET"
    )

    pdf.setFillColor(DARK)

    pdf.setFont("Helvetica-Bold", 7)

    pdf.drawString(
        x + 63 * mm,
        y + 14 * mm,
        "HALL: " + hall
    )

    pdf.drawString(
        x + 110 * mm,
        y + 14 * mm,
        "MOVIE: " + theater
    )

    pdf.drawString(
        x + 145 * mm,
        y + 14 * mm,
        "seat: " + seat
    )

    pdf.saveState()

    pdf.translate(
        x + ticket_width - 5 * mm,
        y + ticket_height / 2
    )

    pdf.rotate(90)

    pdf.setFillColor(colors.white)

    pdf.setFont("Helvetica-Bold", 7)

    pdf.drawCentredString(
        0,
        0,
        ticket_number
    )


    pdf.restoreState()

    pdf.showPage()
    pdf.save()

    print("PDF ticket:", filename)

