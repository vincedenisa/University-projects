#pragma once


#include "in_memory_repo.h"

class FileRepo : public InMemoryRepo {
protected:
    std::string file_name;

    virtual void read_from_file();

    virtual void write_to_file();

    static std::vector<std::string> tokenize(const std::string &str, char delimiter);

public:

    explicit FileRepo(std::string &file_name) : file_name(std::move(file_name)) {};

    TrenchCoat find_trench_coat(std::string &size, std::string &colour) override;

    void add_trench_to_repo(const TrenchCoat &t) override;

    void remove_trench_from_repo(TrenchCoat &t) override;

    void update_trench_in_repo(TrenchCoat &t) override;

    int get_repository_size() override;

    std::vector<TrenchCoat> get_repository_trenches() override;

    virtual void open_file_with_app();

};


