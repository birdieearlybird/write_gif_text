from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io
import sys

# Custom font style and font size
myFont = ImageFont.truetype('Perfect DOS VGA 437.ttf', 20)


def main(argv):

    num_of_shirts = int(sys.argv[1])

    for x in range(num_of_shirts):
        print("Printing shirt #" + str(x+1))
        im = Image.open('images/Shirt-Spin.gif')
        frames = []
    # Loop over each frame in the animated image
        for frame in ImageSequence.Iterator(im):
            frame = frame.convert('RGBA')
            # Draw the text on the frame
            d = ImageDraw.Draw(frame)
            series_text = "#" + str(x + 1) + " of " + str(num_of_shirts)
            d.text((10,10), series_text,  font=myFont, fill=(255,255,255))
            del d

            # However, 'frame' is still the animated image with many frames
            # It has simply been seeked to a later frame
            # For our list of frames, we only want the current frame

            # Saving the image without 'save_all' will turn it into a single frame image, and we can then re-open it
            # To be efficient, we will save it to a stream, rather than to file
            b = io.BytesIO()
            frame.save(b, format="GIF")
            frame = Image.open(b)

            # Then append the single frame image to a list of frames
            frames.append(frame)
        # Save the frames as a new image
        fn = "output/out" + str(x + 1) + ".gif"
        frames[0].save(fn, save_all=True, append_images=frames[1:])

if __name__ == "__main__":
   main(sys.argv[1:])
