import cv2
from pyzbar import pyzbar  # Read barcode and QR codes.


def read_barcodes(frame):
    """ This function does three things:
    1. Recognize and decode the barcode / QR code that we are going to show to the camera.
    2. Added information stored as text on recognized barcode / QR code.
    3. And finally, export the stored information as a text document.
    """
    barcodes = pyzbar.decode(frame)  
    for barcode in barcodes:
        # Recognize the barcode or QR code
        x, y, w, h = barcode.rect                                                      
        # Draw a rectangle around the barcode or QR code
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 

        # Decode the barcode or QR code information
        barcode_info = barcode.data.decode('utf-8') 
        font = cv2.FONT_HERSHEY_PLAIN
        # Add text above the rectangle that has been created
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 1.0, (255, 255, 255), 1) 
        
        # Export the information to a text document.
        with open("Barcode and QR Code Result.txt", mode ='w') as file:
            file.write("Recognized Barcode/QR Code:" + barcode_info + "\n")

    return frame
        


def main():
    print("Please Press q button to quit the program.")
    # Turn on the computer camera
    # If you have an external camera, you need to change the value 0 to 1 depending on the device.
    camera = cv2.VideoCapture(0)                            
    ret, frame = camera.read()
    
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        # Launch the camera that we turned on
        cv2.imshow('Barcode/QR code reader', frame)        
        
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    main()