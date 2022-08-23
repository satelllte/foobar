import base64
from itertools import cycle

message = 'GlQHTVNaXUNKRlNOGBdeSlVYFVRYGBdaV1xVBBITTVUeGAoZRhYHTFVcVVVdRl9UH1VfXl9LFQBT GAoZH1lXAgERXFlbVFUeTVNTWVNRUVVPBB4RVkQeGAoZRgYaVF9aU1VdRl9UH0JYWlJQFQBTGAoZ H0NYBxZTFBAeXl9WRlNOGBdOUV4YRg4='

key = bytes('ast809809', 'utf8')

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
