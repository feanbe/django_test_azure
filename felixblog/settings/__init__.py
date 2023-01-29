from .base import *
# you need to set "myproject = 'production'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ['myproject'] == 'production':
   from .production import *
else:
   from .development import *