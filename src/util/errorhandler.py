# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
logger = logger('Error Handler')

def handle_exception(exc_type, exc_value, exc_traceback):
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logger.error(text=tb)
    
    try:
        requests.post(f'http://prem-eu1.bot-hosting.net:22100/error',
            json={
                'title': 'G4Spam Error',
                'message': tb,
                'script': 'G4Spam',
                'level': 'ERROR',
                'version': version,
                'timestamp': time.time()
            },
            timeout=5
        )

    except:
        pass
    
    logger.log(text='Press enter to quit, if this keeps happening join the discord and report the error (REDOWNLOADING MIGHT FIX THIS ISSUE)', ts=True)
    input('')
    sys.exit()

sys.excepthook = handle_exception