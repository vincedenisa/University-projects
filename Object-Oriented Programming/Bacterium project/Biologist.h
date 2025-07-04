#pragma once
#include <QString>
#include <vector>

class Biologist {
private:
    QString name;
    std::vector<QString> species;
public:
    Biologist(const QString& name, const std::vector<QString>& species) : name(name), species(species) {}
    QString getName() const { return name; }
    const std::vector<QString>& getSpecies() const { return species; }

    bool studiesSpecies(const QString& s) const {
        return std::find(species.begin(), species.end(), s) != species.end();
    }
};
