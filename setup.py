from setuptools import find_packages, setup

package_name = 'distance_lcd'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bhoomishree',
    maintainer_email='bhoomishree@todo.todo',
    description='Distance publisher and LCD subscriber using Arduino and ROS2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         'distance_publisher = distance_lcd.distance_publisher:main',
         'status_subscriber = distance_lcd.status_subscriber:main',
        ],
    },
)
