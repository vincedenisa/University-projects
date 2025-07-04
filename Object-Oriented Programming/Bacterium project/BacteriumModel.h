#pragma once
#include <QAbstractTableModel>
#include "Service.h"

class BacteriumModel : public QAbstractTableModel {
    Q_OBJECT

private:
    Service* service;
    QString speciesFilter;

public:
    //Connects to the service, sets up the model to update on data changes
    BacteriumModel(Service* srv, QObject* parent = nullptr)
        : QAbstractTableModel(parent), service(srv), speciesFilter("") {
        connect(service, &Service::dataChanged, this, [this]() {
            beginResetModel();
            endResetModel();
        });
    }

    // Sets the filter and refreshes the model
    void setSpeciesFilter(const QString& species) {
        speciesFilter = species;
        beginResetModel();
        endResetModel();
    }

    //Returns the no rows that match the filter
    int rowCount(const QModelIndex& parent = QModelIndex()) const override {
        Q_UNUSED(parent);
        return service->getBacteriaBySpecies(speciesFilter).size();
    }

    //Returns the no columns
    int columnCount(const QModelIndex& parent = QModelIndex()) const override {
        Q_UNUSED(parent);
        return 4; // name, species, size, diseases
    }

    //Returns the data that will be displayed in a cell
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
        if (!index.isValid() || role != Qt::DisplayRole)
            return {};

        const auto& list = service->getBacteriaBySpecies(speciesFilter);
        const auto& b = list.at(index.row());

        switch (index.column()) {
        case 0: return b.getName();
        case 1: return b.getSpecies();
        case 2: return QString::number(b.getSize());
        case 3: { QStringList qlist;
            for (const auto& d : b.getDiseases())
                qlist << d;
            return qlist.join(", ");}

        }
        return {};
    }

    //Returns the header for each column
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override {
        if (role != Qt::DisplayRole || orientation != Qt::Horizontal)
            return {};
        switch (section) {
        case 0: return "Name";
        case 1: return "Species";
        case 2: return "Size";
        case 3: return "Diseases";
        }
        return {};
    }
};
