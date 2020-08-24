cmake_minimum_required(VERSION 3.10)

project(lxi_device_control)

add_executable(cpx400sp src/cpx400sp.cc)

include_directories(include/lxi_device_control)

target_link_libraries(cpx400sp lxi)