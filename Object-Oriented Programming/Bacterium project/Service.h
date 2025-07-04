#pragma once
#include "Repository.h"
#include <QObject>

class Service : public QObject {
    Q_OBJECT

private:
    Repository* repo;

public:
    Service(Repository* r, QObject* parent = nullptr);

    const std::vector<Biologist>& getBiologists() const;
    const std::vector<Bacterium>& getBacteria() const;
    std::vector<Bacterium> getBacteriaBySpecies(const QString& species) const;

    void addBacterium(const Bacterium& b);
    void updateBacterium(const QString& name, const Bacterium& updated);
    void saveAll(const QString& bacteriaFile);

signals:
    void dataChanged();
};
