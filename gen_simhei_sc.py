import utils
import shutil as fs

def gen_simhei_sc(path):
    font = utils.open_font(path + '/SarasaUiSC-Regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_simhei_names(font)

    font.generate(path + '/simhei.ttf')
