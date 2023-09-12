import os
import io
import textwrap
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

current_folder = os.path.dirname (__file__)
parent_folder = os.path.dirname (current_folder)
files_folder = os.path.join (parent_folder, "static")
original_pdf = os.path.join (current_folder, f"book_template_1.pdf")
emilya_font = os.path.join (current_folder, f"emilya_birthday.ttf")
pete_font = os.path.join (current_folder, f"pete_15.ttf")
arial_font = os.path.join (current_folder, f"arial_bold.ttf")

def custom_wrap(text, width):
    # Split text at newline characters
    lines = text.split('\n')
    
    # Wrap each line to fit the given width
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    
    # Join the wrapped lines back together
    return '\n'.join(wrapped_lines)
	
def generatePDF(child_name, child_fullname, date, dedication):
	packet = io.BytesIO()
	
	pdfmetrics.registerFont(TTFont('emilya', emilya_font))
	pdfmetrics.registerFont(TTFont('pete', pete_font))
	pdfmetrics.registerFont(TTFont('arial', arial_font))

	c = canvas.Canvas(packet, letter)

	encabezado1 = f"Dear {child_name}"
	encabezado2 = f"{dedication}"
	encabezado3 = "adventure and fun."
	encabezado4 = "I will allways love you"
	encabezado5 = "precious little one."

	#Portada
	custom_page_size = (1200, 1000)
	c.setPageSize(custom_page_size)
	c.setFillColorRGB(1, 1, 0.2, 1)
	c.setFont('emilya', 50)
	c.drawString(255-(len(child_name)/2)*7.5, 360, child_name)
	c.setFont('emilya', 110)
	c.drawString(800-(len(child_name)/2)*10, 390, child_name)

	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")

	c.showPage()

	dedication='Dear Viewer,' + '\n' + 'you can add your hand written dedication here - or if you provide us your dedication message we will print it here for you.' + '\n' + 'BelovedCo Team'	
	#dedication = custom_wrap(dedication, 30)
	wrapper = textwrap.TextWrapper(width=30)
	word_list = wrapper.wrap(text = dedication)
	position = 500
	
	#Página 1
	c.setFont('pete', 25)
	for element in word_list:
		element = element.replace('NEWLINE','\n')					
		c.drawString(800-(len(element)/2)*7.5, position, element)		
		position-=40
	
	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")

	c.showPage()
	
	#Página 2
	c.setFont('pete', 30)
	c.drawString(250-(len(child_fullname)/2)*7.5, 270, child_fullname)
	c.drawString(250-(len(date)/2)*7.5, 230, date)

	encabezado1 = "Ten little fingers"
	encabezado2 = "Ten tiny toes"
	encabezado3 = f"{child_name} you are perfect"
	encabezado4 = "With a cute button nose"

	c.setFont('pete', 30)
	c.setFillColorRGB(0, 0, 0, 1)
	c.drawString(720-(len(encabezado1)/2)*7.5, 640, encabezado1)
	c.drawString(720-(len(encabezado2)/2)*7.5, 600, encabezado2)
	c.drawString(700-(len(encabezado3)/2)*7.5, 560, encabezado3)
	c.drawString(700-(len(encabezado4)/2)*7.5, 520, encabezado4)

	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")	

	c.showPage()

	for i in range(2):
		c.setFont('arial', 120)
		c.setFillColorRGB(0, 0, 0, 0.2)
		c.drawString(275, 400, "SAMPLE")
	
		c.showPage()

	encabezado1 = f"{child_name} you are"
	encabezado2 = "A bright shining star"
	encabezado3 = "You light up our life"
	encabezado4 = "Our own superstar"

	#Página 3
	c.setFont('pete', 30)
	c.setFillColorRGB(255, 255, 255, 1)
	c.drawString(190-(len(encabezado1)/2)*7.5, 210, encabezado1)
	c.drawString(190-(len(encabezado2)/2)*7.5, 170, encabezado2)
	c.drawString(220-(len(encabezado3)/2)*7.5, 130, encabezado3)
	c.drawString(240-(len(encabezado4)/2)*7.5, 90, encabezado4)

	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")

	c.showPage()

	for i in range(8):
		c.setFont('arial', 120)
		c.setFillColorRGB(0, 0, 0, 0.2)
		c.drawString(275, 400, "SAMPLE")

		c.showPage()

	encabezado1 = f"But for now {child_name}"
	encabezado2 = "We'll wait for the adventures you'll take"

	#Página 4
	c.setFont('pete', 25)
	c.setFillColorRGB(255, 255, 255, 1)
	c.drawString(260-(len(encabezado1)/2)*7.5, 130, encabezado1)
	c.drawString(260-(len(encabezado2)/2)*7.5, 100, encabezado2)

	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")	

	c.showPage()

	encabezado1 = f"{child_name} our sweet gift"
	encabezado2 = "That we love and adore"
	encabezado3 = "As the days go by"
	encabezado4 = "We love you more and more"


	#Página 5
	c.setFont('pete', 25)
	c.drawString(260-(len(encabezado1)/2)*7.5, 160, encabezado1)
	c.drawString(255-(len(encabezado2)/2)*7.5, 130, encabezado2)
	c.drawString(270-(len(encabezado3)/2)*7.5, 100, encabezado3)
	c.drawString(260-(len(encabezado4)/2)*7.5, 70, encabezado4)

	c.setFont('arial', 120)
	c.setFillColorRGB(0, 0, 0, 0.2)
	c.drawString(275, 400, "SAMPLE")

	c.showPage()

	for i in range(3):
		c.setFont('arial', 120)
		c.setFillColorRGB(0, 0, 0, 0.2)
		c.drawString(275, 400, "SAMPLE")

		c.showPage()

	c.save()

	packet.seek(0)

	new_pdf = PdfFileReader(packet)

	existing_pdf = PdfFileReader(open(original_pdf, "rb"))
	output = PdfFileWriter()
	
	for i in range(0, 17):
		page = existing_pdf.pages[i]
		page.merge_page(new_pdf.pages[i])
		output.add_page(page)

	new_pdf = os.path.join (files_folder, f"{child_name}.pdf")
	output_stream = open(new_pdf, "wb")
	output.write(output_stream)
	output_stream.close()
	
if __name__=='__main__':
	generatePDF("Name","Here is an example full name", "17 February 2017", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus, perferendis dicta, maxime repellendus cupiditate facilis sequi numquam alias hic excepturi tenetur, inventore unde enim. Ipsum magnam beatae consequatur corrupti asperiores architecto neque saepe reiciendis ad nostrum in natus sapie")
