#pragma once
#include <QString>
#include <vector>

class Bacterium{
private:
    QString name;
    QString species;
    int size;
    std::vector<QString> diseases;

public:
    Bacterium(const QString& name, const QString& species, int size, const std::vector<QString>& diseases)
        : name(name), species(species), size(size), diseases(diseases) {}

    QString getName() const {return name;}
    QString getSpecies() const{ return species;}
    int getSize() const { return size; }
    const std::vector<QString>& getDiseases() const { return diseases; }



    void setSpecies(const QString& s) { species = s; }
    void setSize(int s) { size = s; }
    void setDiseases(const std::vector<QString>& d) { diseases = d; }
    void addDisease(const QString& disease) { diseases.push_back(disease); }
};


