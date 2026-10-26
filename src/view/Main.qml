import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Python + QML"

    Button {
        anchors.centerIn: parent
        text: "Click Me"
        // Calls the Python method mapped to this view
        onClicked: pythonBackend.on_button_clicked() 
    }
}