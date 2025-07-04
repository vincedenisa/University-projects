#include <QVBoxLayout>
#include <QFormLayout>
#include <QGridLayout>
#include <QErrorMessage>
#include <QMessageBox>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>
#include <QLineEdit>
#include "GUI.h"

// removed: #include <QtCharts/...> and using namespace QtCharts

// removed: AdminGUI::displayChart() and chartButton related code

void AdminGUI::initAdminGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>ADMIN MODE</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(10);
    titleFont.setStyleHint(QFont::System);
    titleFont.setWeight(QFont::Medium);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    layout->addWidget(this->dogsListWidget);

    auto* dogDetailsLayout = new QFormLayout{};
    dogDetailsLayout->addRow("Name", this->nameLineEdit);
    dogDetailsLayout->addRow("Breed", this->breedLineEdit);
    dogDetailsLayout->addRow("Age", this->ageLineEdit);
    dogDetailsLayout->addRow("Link", this->linkLineEdit);
    layout->addLayout(dogDetailsLayout);

    auto* buttonsLayout = new QGridLayout{};
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 1);
    buttonsLayout->addWidget(this->updateButton, 1, 0);
    layout->addLayout(buttonsLayout); // removed chartButton
}

void AdminGUI::connectSignalsAndSlots() {
    QObject::connect(this->dogsListWidget, &QListWidget::itemSelectionChanged, [this]() {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        Dog dog = this->service.getAllService()[selectedIndex];
        this->nameLineEdit->setText(QString::fromStdString(dog.nameGetter()));
        this->breedLineEdit->setText(QString::fromStdString(dog.breedGetter()));
        this->ageLineEdit->setText(QString::fromStdString(std::to_string(dog.ageGetter())));
        this->linkLineEdit->setText(QString::fromStdString(dog.photoGetter()));
        });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminGUI::addDog);
    QObject::connect(this->deleteButton, &QPushButton::clicked, this, &AdminGUI::deleteDog);
    QObject::connect(this->updateButton, &QPushButton::clicked, this, &AdminGUI::updateDog);
    // removed chartButton connection
}
AdminGUI::AdminGUI(QWidget* parent, Service& serv, DogValidator& validator1, Repository& repo)
    : service{ serv }, validator{ validator1 }, repository{ repo } {
    this->titleWidget = new QLabel(this);
    this->dogsListWidget = new QListWidget{};
    this->nameLineEdit = new QLineEdit{};
    this->breedLineEdit = new QLineEdit{};
    this->ageLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add");
    this->deleteButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");
    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initAdminGUI();
    this->populateList();
    this->connectSignalsAndSlots();
    this->listModel = new DogListModel{ this->repository };
}

AdminGUI::~AdminGUI() = default;

int AdminGUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->dogsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->nameLineEdit->clear();
        this->breedLineEdit->clear();
        this->ageLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    return selectedIndexes.at(0).row();
}

void AdminGUI::addDog() {
    std::string breed = this->breedLineEdit->text().toStdString();
    std::string name = this->nameLineEdit->text().toStdString();
    std::string age_s = this->ageLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();
    int age;
    try {
        this->validator.validateBreed(breed);
        this->validator.validateName(name);
        this->validator.validateAgeString(age_s);
        age = stoi(age_s);
        this->validator.validateAge(age);
        this->validator.validatePhotoLink(link);
        this->service.addService(breed, name, age, link);
        this->populateList();
    }
    catch (ValidationException& exc) {
        QMessageBox::critical(this, "Invalid input!", exc.what());
    }
    catch (RepositoryException& re) {
        QMessageBox::critical(this, "Error at adding dog!", re.what());
    }
}

void AdminGUI::deleteDog() {
    try {
        std::string name = this->nameLineEdit->text().toStdString();
        this->validator.validateName(name);
        this->service.deleteService(name);
        this->populateList();
    }
    catch (ValidationException& exc) {
        QMessageBox::critical(this, "Invalid input!", exc.what());
    }
    catch (RepositoryException& re) {
        QMessageBox::critical(this, "Error at deleting dog!", re.what());
    }
}

void AdminGUI::updateDog() {
    int index = this->getSelectedIndex();
    try {
        if (index < 0) {
            QMessageBox::critical(this, "Selection error!", "No dog selected!");
            return;
        }
        std::string old_name = this->service.getAllService()[index].nameGetter();
        std::string new_name = this->nameLineEdit->text().toStdString();
        std::string new_breed = this->breedLineEdit->text().toStdString();
        std::string age_s = this->ageLineEdit->text().toStdString();
        std::string new_link = this->linkLineEdit->text().toStdString();
        int age = std::stoi(age_s);

        this->validator.validateName(old_name);
        this->validator.validateName(new_name);
        this->validator.validateBreed(new_breed);
        this->validator.validateAgeString(age_s);
        this->validator.validateAge(age);
        this->validator.validatePhotoLink(new_link);

        this->service.updateService(old_name, new_breed, new_name, age, new_link);
        this->populateList();
    }
    catch (ValidationException& exc) {
        QMessageBox::critical(this, "Invalid input!", exc.what());
    }
    catch (RepositoryException& re) {
        QMessageBox::critical(this, "Error at updating dog!", re.what());
    }
}
void AdminGUI::populateList() {
	this->dogsListWidget->clear();
	std::vector<Dog> dogs = this->service.getAllService();
	for (const Dog& dog : dogs) {
		this->dogsListWidget->addItem(QString::fromStdString(dog.nameGetter()));
	}
	if (!dogs.empty()) {
		this->dogsListWidget->setCurrentRow(0);
	}
}
GUI::GUI(Service& serv, UserService& userserv, DogValidator& validator1, Repository& repository)
    : service{ serv }, userService{ userserv }, validator{ validator1 }, repository{ repository } {
    this->titleWidget = new QLabel(this);
    this->adminButton = new QPushButton(this);
    this->userButton = new QPushButton(this);
    this->initGUI();
    this->connectSignalsAndSlots();
}

GUI::~GUI() = default;

void GUI::showAdmin() {
    auto* admin = new AdminGUI(this, this->service, this->validator, this->repository);
    admin->show();
}

void GUI::showUser() {
    auto* user = new UserGUI(this, this->service, this->userService, this->validator);
    user->show();
}
void GUI::initGUI() {
	auto* layout = new QVBoxLayout(this);
	QFont titleFont = this->titleWidget->font();
	this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>Dog Shelter</font></p>");
	titleFont.setItalic(true);
	titleFont.setPointSize(10);
	titleFont.setStyleHint(QFont::System);
	titleFont.setWeight(QFont::Medium);
	this->titleWidget->setFont(titleFont);
	layout->addWidget(this->titleWidget);
    int DogListModel::rowCount(const QModelIndex & parent) const {
        Q_UNUSED(parent);
        return this->repository.getAllRepo().size();
    }

	this->adminButton->setText("Admin Mode");
	this->userButton->setText("User Mode");
	layout->addWidget(this->adminButton);
	layout->addWidget(this->userButton);
}
void GUI::connectSignalsAndSlots() {
	QObject::connect(this->adminButton, &QPushButton::clicked, this, &GUI::showAdmin);
	QObject::connect(this->userButton, &QPushButton::clicked, this, &GUI::showUser);
}

QVariant DogListModel::data(const QModelIndex& index, int role) const {
	if (!index.isValid() || index.row() < 0 || index.row() >= this->repository.getNrElems()) {
		return QVariant();
	}
	if (role == Qt::DisplayRole) {
		const Dog& dog = this->repository.getAllRepo()[index.row()];
		return QString::fromStdString(dog.nameGetter());
	}
	return QVariant();
}
