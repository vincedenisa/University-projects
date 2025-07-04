#include "Repository.h"

void Repository::loadBiologists(const QString& filename) {
    biologists.clear();
    QFile file(filename);
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream in(&file);
        while (!in.atEnd()) {
            QString line = in.readLine();
            auto parts = line.split(";"); // split by ";"
            if (parts.size() >= 2) {
                QString name = parts[0].trimmed(); //Biologist naem
                std::vector<QString> species;
                for (int i = 1; i < parts.size(); ++i)
                    species.push_back(parts[i].trimmed()); // All studied species
                biologists.emplace_back(name, species); //Add biologist to list
            }
        }
    }
}

void Repository::loadBacteria(const QString& filename) {
    bacteria.clear();
    QFile file(filename);
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream in(&file);
        while (!in.atEnd()) {
            QString line = in.readLine();
            auto parts = line.split(";");
            if (parts.size() >= 4) {
                QString name = parts[0].trimmed();
                QString species = parts[1].trimmed();
                int size = parts[2].trimmed().toInt();
                std::vector<QString> diseases;
                for (int i = 3; i < parts.size(); ++i)
                    diseases.push_back(parts[i].trimmed());
                bacteria.emplace_back(name, species, size, diseases);
            }
        }
    }
    emit dataChanged(); //Notify observers of the update
}

void Repository::saveBacteria(const QString& filename) {
    QFile file(filename);
    if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        QTextStream out(&file);
        for (const auto& b : bacteria) {
            out << b.getName() << ";" << b.getSpecies() << ";" << b.getSize();
            for (const auto& d : b.getDiseases())
                out << ";" << d; //Append each disease
            out << "\n";// new line for new bacteria
        }
    }
}

const std::vector<Biologist>& Repository::getBiologists() const {
    return biologists;
}

const std::vector<Bacterium>& Repository::getBacteria() const {
    return bacteria;
}

void Repository::addBacterium(const Bacterium& b) {
    for (const auto& existing : bacteria) {
        if (existing.getName() == b.getName() && existing.getSpecies() == b.getSpecies())
            throw std::runtime_error("Bacterium already exists");
    }
    bacteria.push_back(b);
    emit dataChanged(); // Notify ui models/views
}

void Repository::updateBacterium(const QString& name, const Bacterium& updated) {
    for (auto& b : bacteria) {
        if (b.getName() == name) {
            b.setSpecies(updated.getSpecies());
            b.setSize(updated.getSize());
            b.setDiseases(updated.getDiseases());
            emit dataChanged();// Notify observers
            return;
        }
    }
    throw std::runtime_error("Bacterium not found");
}
