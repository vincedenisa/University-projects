#include <QApplication>
#include "Service.h"
#include "Repository.h"
#include "BiologistWindow.h"

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);

    Repository* repo = new Repository;
    repo->loadBiologists(R"(C:\faculta\oop_25\exam_oop\build\Desktop_Qt_6_9_0_MinGW_64_bit-Debug\debug\biologists.txt)");
    repo->loadBacteria(R"(C:\faculta\oop_25\exam_oop\build\Desktop_Qt_6_9_0_MinGW_64_bit-Debug\debug\bacteria.txt)");

    Service* service = new Service(repo);

    QList<BiologistWindow*> windows;
    for (const auto& b : repo->getBiologists()) {
        BiologistWindow* w = new BiologistWindow(service, b);
        w->show();
        windows.append(w);
    }

    int result = app.exec();

    service->saveAll(R"(C:\faculta\oop_25\exam_oop\build\Desktop_Qt_6_9_0_MinGW_64_bit-Debug\debug\bacteria.txt)");

    qDeleteAll(windows);
    delete service;
    delete repo;

    return result;
}
