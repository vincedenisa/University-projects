#include "Service.h"

Service::Service(Repository* r, QObject* parent)
    : QObject(parent), repo(r) {
    connect(repo, &Repository::dataChanged, this, &Service::dataChanged);
}

const std::vector<Biologist>& Service::getBiologists() const {
    return repo->getBiologists();
}

const std::vector<Bacterium>& Service::getBacteria() const {
    return repo->getBacteria();
}

std::vector<Bacterium> Service::getBacteriaBySpecies(const QString& species) const {
    if (species.isEmpty())
        return repo->getBacteria();

    std::vector<Bacterium> result;
    for (const auto& b : repo->getBacteria())
        if (b.getSpecies() == species)
            result.push_back(b);
    return result;
}

void Service::addBacterium(const Bacterium& b) {
    for (const auto& existing : repo->getBacteria())
        if (existing.getName() == b.getName() && existing.getSpecies() == b.getSpecies())
            throw std::runtime_error("Bacterium with same name and species already exists!");

    repo->addBacterium(b);
}

void Service::updateBacterium(const QString& name, const Bacterium& updated) {
    repo->updateBacterium(name, updated);
}

void Service::saveAll(const QString& bacteriaFile){
    repo->saveBacteria(bacteriaFile);
}
