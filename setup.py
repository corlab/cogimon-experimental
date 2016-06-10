# ============================================================
#
# Copyright (C) 2016 by Johannes Wienke <jwienke at techfak dot uni-bielefeld dot de>
#
# This file may be licensed under the terms of the
# GNU Lesser General Public License Version 3 (the ``LGPL''),
# or (at your option) any later version.
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the LGPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the LGPL along with this
# program. If not, go to http://www.gnu.org/licenses/lgpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# The development of this software was supported by:
#   CoR-Lab, Research Institute for Cognition and Robotics
#     Bielefeld University
#
# ============================================================

from setuptools import setup, find_packages


VERSION = '1.0'

setup(name='cogimon-experimental',
      version=VERSION,
      description='''
                  Experimental tools and modules developed in the CogIMon EU Project.
                  ''',
      author='Dennis Wigand, Sebastian Wrede',
      author_email='dwigand@techfak.uni-bielefeld.de',
      license='LGPLv3+',
      keywords=['robotics', 'rsb', 'cogimon'],
      classifiers=['Programming Language :: Python'],

      install_requires=['rsb-python>=0.14',
                        'rststable>=0.14',
                        'rstsandbox>=0.14',
                        'loggerbyclass>=0.2'],

      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,

      entry_points={
          'console_scripts':
              ['rsb-jointangle-sender{version} = '
               'cogimontools.jointanglesender:main'.format(version=VERSION),
               'rsb-robot-gui{version} = '
               'cogimontools.robotgui:main'.format(version=VERSION)]
      })
