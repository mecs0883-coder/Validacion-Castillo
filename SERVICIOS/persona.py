from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from DATOS.persona_DAO import PersonaDAO
from DOMINIO.persona import Persona
from UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    '''
    clase que genera la logica de los objetos
    '''
    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)

        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)

        self.ui.txtCedula.setValidator(QIntValidator())

        regex = QRegularExpression(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        email_validator = QRegularExpressionValidator(regex)
        self.ui.txtEmail.setValidator(email_validator)

    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.cbsexo.currentText()
        email = self.ui.txtEmail.text()

        if nombre == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el nombre')
            return
        if apellido == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el apellido')
            return
        if len(cedula) < 10:
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar la cédula (10 dígitos)')
            return
        if sexo == "Seleccionar":
            QMessageBox.warning(self, 'Advertencia', 'Debe seleccionar el sexo')
            return

        try:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, email=email, sexo=sexo)
            # PersonaDAO.insertar_persona(persona)
            print(persona)

            self.ui.statusbar.showMessage('Se guardó la información', 3000)
            self.limpiar()

        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

    def limpiar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtCedula.setText('')
        self.ui.txtEmail.setText('')
        self.ui.cbsexo.setCurrentText('Seleccionar')