#pragma once
#include "Service.h"
#include "BacteriumModel.h"
#include <QWidget>
#include <QTableView>
#include <QPushButton>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QFormLayout>
#include <QComboBox>
#include <QMessageBox>

class BiologistWindow : public QWidget {
    Q_OBJECT

private:
    Service* service;
    QString biologistName;
    BacteriumModel* model;
    QTableView* table;
    QComboBox* speciesFilterBox;
    QLineEdit *nameEdit, *speciesEdit, *sizeEdit, *diseasesEdit;
    QPushButton *addButton, *updateButton;

public:
    BiologistWindow(Service* srv, const Biologist& bio, QWidget* parent = nullptr)
        : QWidget(parent), service(srv), biologistName(bio.getName()) {
        setWindowTitle("Biologist: " + biologistName);
        model = new BacteriumModel(service, this);

        QVBoxLayout* layout = new QVBoxLayout(this);

        // Filter dropdown
        speciesFilterBox = new QComboBox;
        speciesFilterBox->addItem("");

        //Populate species list
        QSet<QString> allSpecies;
        for (const auto& b : service->getBacteria())
            allSpecies.insert(b.getSpecies());
        for (const auto& s : allSpecies)
            speciesFilterBox->addItem(s);
        layout->addWidget(speciesFilterBox);

        //Connect dropdown to model
        connect(speciesFilterBox, &QComboBox::currentTextChanged, this, [=](const QString& selected) {
            model->setSpeciesFilter(selected);
        });

        //TableView
        table = new QTableView;
        table->setModel(model);
        layout->addWidget(table);

        //Input form
        QFormLayout* form = new QFormLayout;
        nameEdit = new QLineEdit;
        speciesEdit = new QLineEdit;
        sizeEdit = new QLineEdit;
        diseasesEdit = new QLineEdit;
        form->addRow("Name:", nameEdit);
        form->addRow("Species:", speciesEdit);
        form->addRow("Size:", sizeEdit);
        form->addRow("Diseases (comma separated):", diseasesEdit);
        layout->addLayout(form);

        //Buttons
        QHBoxLayout* buttonLayout = new QHBoxLayout;
        addButton = new QPushButton("Add");
        updateButton = new QPushButton("Update");
        buttonLayout->addWidget(addButton);
        buttonLayout->addWidget(updateButton);
        layout->addLayout(buttonLayout);

        //Connect buttons to handlers
        connect(addButton, &QPushButton::clicked, this, &BiologistWindow::handleAdd);
        connect(updateButton, &QPushButton::clicked, this, &BiologistWindow::handleUpdate);
    }

private slots:
    void handleAdd() {
        try {
            QString name = nameEdit->text();
            QString species = speciesEdit->text();
            int size = sizeEdit->text().toInt();

            //Split diseases by ",", remove whitespace
            QStringList diseaseList = diseasesEdit->text().split(",", Qt::SkipEmptyParts);
            std::vector<QString> diseases;
            for (const auto& d : diseaseList)
                diseases.push_back(d.trimmed());

            //Add new bacteria through service
            service->addBacterium(Bacterium(name, species, size, diseases));
        } catch (const std::exception& e) {
            QMessageBox::warning(this, "Error", e.what());
        }
    }

    void handleUpdate() {
        try {
            QString name = nameEdit->text();
            QString species = speciesEdit->text();
            int size = sizeEdit->text().toInt();
            QStringList diseaseList = diseasesEdit->text().split(",", Qt::SkipEmptyParts);
            std::vector<QString> diseases;
            for (const auto& d : diseaseList)
                diseases.push_back(d.trimmed());

            //Update via service
            service->updateBacterium(name, Bacterium(name, species, size, diseases));
        } catch (const std::exception& e) {
            QMessageBox::warning(this, "Error", e.what());
        }
    }
};
