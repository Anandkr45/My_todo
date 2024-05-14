import PySimpleGUI as sg

label1 = sg.Text("Select file to compress")
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select file to compress")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")
bg_color = sg.theme_background_color('purple')

window = sg.Window("File Compressor", layout=[[label1, input1, choose_btn1],
                                              [label2, input2, choose_btn2],
                                              [compress_btn]])

window.read()
window.close()