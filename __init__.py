from os.path import dirname, join

from tvprogram_skill.index import tvprogram
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class TVProgramSkill(OnyxSkill):
    def __init__(self):
        super(TVProgramSkill, self).__init__(name="TVProgramSkill")

    def get_blueprint(self):
        return tvprogram

    def initialize(self):
        LOGGER.info("TVProgram Skill initialize")

    def stop(self):
        pass

def create_skill():
    return TVProgramSkill()
