PyMoDAQ Utils
#############

.. image:: https://img.shields.io/pypi/v/pymodaq_utils.svg
   :target: https://pypi.org/project/pymodaq_utils/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/pymodaq/badge/?version=latest
   :target: https://pymodaq.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://codecov.io/gh/PyMoDAQ/pymodaq_utils/branch/0.0.x/graph/badge.svg?token=IQNJRCQDM2
    :target: https://codecov.io/gh/PyMoDAQ/PyMoDAQ

====== ========== ======= ======
Python Qt Backend OS      Passed
====== ========== ======= ======
3.8    Qt5        Linux   |38Qt5|
3.9    Qt5        Linux   |39Qt5|
3.10   Qt5        Linux   |310Qt5|
3.11   Qt5        Linux   |311Qt5|
3.8    Qt5        Windows |38Qt5win|
3.8    PySide2    Linux   |38pyside|
3.9    Qt6        Linux   |39Qt6|
====== ========== ======= ======


.. |38Qt5| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyqt5.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyqt5.yml

.. |39Qt5| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp39pyqt5.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp39pyqt5.yml

.. |310Qt5| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp310pyqt5.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp310pyqt5.yml

.. |311Qt5| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp311pyqt5.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp311pyqt5.yml

.. |38Qt5win| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyqt5_win.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyqt5_win.yml

.. |38pyside| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyside2.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp38pyside2.yml

.. |39Qt6| image:: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp39pyqt6.yml/badge.svg?branch=pymodaq-dev
    :target: https://github.com/PyMoDAQ/pymodaq_utils/actions/workflows/Testp39pyqt6.yml



.. figure:: http://pymodaq.cnrs.fr/en/latest/_static/splash.png
   :alt: shortcut


PyMoDAQ__, Modular Data Acquisition with Python, is a set of **python** modules used to interface any kind of
experiments. It simplifies the interaction with detector and actuator hardware to go straight to the data acquisition
of interest.

__ https://pymodaq.readthedocs.io/en/stable/?badge=latest

This present repository `pymodaq_utils` is a set of utilities (constants, methods and classes) that are used in the
various subpackages of PyMoDAQ (PyMoDAQ itself, but also plugins and data management and user interfaces modules)

PyMoDAQ Diagram:

.. figure:: http://pymodaq.cnrs.fr/en/latest/_images/pymodaq_diagram.png
   :alt: overview

   PyMoDAQ's Dashboard and its extensions: DAQ_Scan for automated acquisitions, DAQ_Logger for data logging and many other.


Published under the MIT FREE SOFTWARE LICENSE

GitHub repo: https://github.com/PyMoDAQ

Documentation: http://pymodaq.cnrs.fr/
