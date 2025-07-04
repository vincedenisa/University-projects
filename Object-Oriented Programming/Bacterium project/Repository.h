#pragma once
#include "Biologist.h"
#include "Bacterium.h"
#include <vector>
#include <QString>
#include <QFile>
#include <QTextStream>
#include <QObject>

class Repository : public QObject {
    Q_OBJECT

private:
    std::vector<Biologist> biologists;
    std::vector<Bacterium> bacteria;

public:
    Repository(QObject* parent = nullptr) : QObject(parent) {}

    void loadBiologists(const QString& filename);
    void loadBacteria(const QString& filename);
    void saveBacteria(const QString& filename);

    const std::vector<Biologist>& getBiologists() const;
    const std::vector<Bacterium>& getBacteria() const;

    void addBacterium(const Bacterium& b);
    void updateBacterium(const QString& name, const Bacterium& updated);

signals:
    void dataChanged();
};
