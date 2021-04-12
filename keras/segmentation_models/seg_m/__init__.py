from . import base
import keras
base.KerasObject.set_submodules(
    backend=keras.backend,
    layers=keras.layers,
    models=keras.models,
    utils=keras.utils
)

from . import metrics