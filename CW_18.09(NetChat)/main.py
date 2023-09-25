#import router 

#route = router.Router()
#route.start()

#import router as r 

#route = r.Router()
#route.start()

import sys
from PyQt6.QtWidgets import QApplication
from router import Router 


if __name__ == "__main__":
    app = QApplication(sys.argv)

    router = Router()
    router.start()
    
    app.exec()







