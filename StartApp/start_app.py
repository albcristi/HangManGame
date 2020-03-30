from UserInterface.user_interface import *
from SentenceController.sentence_controller import *

controller = SentenceController(repostitory_sentence())

interface = ui()
interface.app_exe(controller)