import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')
imgfilename = 'images/DHVANI.jpg'
imgbytes = image_helpers.get_image_from_file(imgfilename)
rekresp = client.detect_faces(Image = {'Bytes': imgbytes} , Attributes = ['ALL'])
pprint(rekresp)
