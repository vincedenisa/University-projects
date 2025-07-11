#pragma once

#include "sqlite3.h"
#include "abstract_repository.h"

class SQLRepo : public AbstractRepository {
private:
    std::string db_file_name;
    sqlite3 *database{};
public:
    explicit SQLRepo(std::string &file_name);

    ~SQLRepo() override;

    TrenchCoat find_trench_coat(std::string &size, std::string &colour) override;

    void add_trench_to_repo(const TrenchCoat &t) override;

    void remove_trench_from_repo(TrenchCoat &t) override;

    void update_trench_in_repo(TrenchCoat &t) override;

    int get_repository_size() override;

    std::vector<TrenchCoat> get_repository_trenches() override;
};


