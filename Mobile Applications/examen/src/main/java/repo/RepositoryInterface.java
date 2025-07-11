package repo;

import exceptions.MyException;
import model.ProgramState;

import java.util.List;

public interface RepositoryInterface {
    //ProgramState getCurrentProgram();
    void addProgram(ProgramState state);
    void logProgramStateExecution(ProgramState state) throws MyException;

    List<ProgramState> getProgramList();
    void setProgramList(List<ProgramState> list);
    ProgramState getProgramStateWithId(int currentId);
}
