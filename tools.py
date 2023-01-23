
def  grid():
    stroke(180)
    for i in range(0, height / 10):
        line(0, 20 + i * 20, width, 20 + i * 20)
        
        
    for i in range(0, width / 10):
        line(20 + i * 20, 0, 20 + i * 20, height)
    
a = 4

def bb():
    strokeWeight(3)
    for i in range(a):
        line(500, 380, 500, 340 - i * 40)
        line(500, 380, 540 + i * 40, 380)

        line(490, 340 - i * 40, 510, 340 - i * 40)
        line(540 + i * 40, 392, 540 + i * 40, 368)
    
        line(460- i * 40, 380, 500 , 380)
        line(460 - i * 40, 368, 460 - i * 40, 392)

        line(500, 380, 500, 420 + i * 40)
        line(490, 420 + i * 40, 510, 420 + i * 40) 
