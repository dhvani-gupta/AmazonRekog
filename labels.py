import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')
imgurl = 'https://th.bing.com/th/id/OIP.vRT6zthWU1RFtx0NOT6YEgHaEm?pid=ImgDet&rs=1'
imgbytes = image_helpers.get_image_from_url(imgurl)
rekresp = client.detect_labels(Image = {'Bytes': imgbytes} , MinConfidence = 1)
#pprint(rekresp)
print("Here are the contents:")
for label in rekresp['Labels']:
    print(label['Name'])