import copy
import re

from like_rubyVisitor import like_rubyVisitor
# from visitors.value_visitor import ValueVisitor
# from visitors.function_visitor import FunctionVisitio
from AST.AstProgramm import AstProgramm
from AST.AstFunction import AstFunction
from AST.AstIntAssignment import AstIntAssignment
from AST.AstStringAssignment import AstStringAssignment
from AST.AstFloatAssignment import AstFloatAssignment
from AST.AstTableAssignment import AstTableAssignment
from AST.AstColumnAssignment import AstColumnAssignment
from AST.AstRowAssignment import AstRowAssignment
from AST.AstFunctionCall import AstFunctionCall
from AST.AstForStatement import AstForStatement
from AST.AstVariable import AstVariable
from AST.AstIfStatement import AstIfStatement
from like_rubyLexer import like_rubyLexer
from like_rubyParser import like_rubyParser
from namespace import Namespace


class Visitor(like_rubyVisitor):
  def __init__(self):
    self.memory = {}
    self.memory['local_values'] = []
    self.memory['defined_function_name'] = []
    self.memory['declared_function_name'] = []
    self.memory['errors'] = []
    self.memory["programm"] = []
    self.programm = AstProgramm()
    self.assignment = 0
    self.function_name = 0
    self.int_assignments = []
    self.float_assignments = []
    self.string_assignments = []
    self.table_assignments = []
    self.column_assignments = []
    self.row_assignments = []
    self.assignments = []
    self.function_calls = []
    self.for_statement = []
    self.if_statements = []

  # Visit a parse tree produced by like_rubyParser#prog.
  def visitProg(self, ctx:like_rubyParser.ProgContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by like_rubyParser#function_definition_list.
  def visitFunction_definition_list(self, ctx:like_rubyParser.Function_definition_listContext):
    for child in ctx.children:
        if child.__class__.__name__ == "Function_definition_headerContext":
            self.programm.declared_function_names.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#expression_list.
  def visitExpression_list(self, ctx:like_rubyParser.Expression_listContext):
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    func.expressions.append(child)
            return self.visitChildren(ctx)
    if ctx in self.programm.expressions:
        self.programm.remove_expression(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminatorContext':
                self.programm.add_expression(child)
    else:
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminatorContext':
                self.programm.add_expression(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#expression.
  def visitExpression(self, ctx:like_rubyParser.ExpressionContext):
    if ctx in self.programm.expressions:
        self.programm.remove_expression(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminatorContext':
                self.programm.add_expression(child)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    func.expressions.append(child)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.expressions.append(child)
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            stat.if_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.if_expressions.append(child)
        if ctx in stat.else_expressions:
            stat.else_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.else_expressions.append(child)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAA--AAAAAAAAAAAAAAAAAAAAAAAAAAA")
        stat.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#global_get.
  def visitGlobal_get(self, ctx:like_rubyParser.Global_getContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#global_set.
  def visitGlobal_set(self, ctx:like_rubyParser.Global_setContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#global_result.
  def visitGlobal_result(self, ctx:like_rubyParser.Global_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_inline_call.
  def visitFunction_inline_call(self, ctx:like_rubyParser.Function_inline_callContext):
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                func.expressions.append(child)
            return self.visitChildren(ctx)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                stat.expressions.append(child)
            return self.visitChildren(ctx)
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            stat.if_expressions.remove(ctx)
            for child in ctx.children:
                stat.if_expressions.append(child)
        if ctx in stat.else_expressions:
            stat.else_expressions.remove(ctx)
            for child in ctx.children:
                stat.else_expressions.append(child)
            return self.visitChildren(ctx)
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            self.programm.expressions.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#require_block. Don't do this
  def visitRequire_block(self, ctx:like_rubyParser.Require_blockContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#pir_inline.
  def visitPir_inline(self, ctx:like_rubyParser.Pir_inlineContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#pir_expression_list.
  def visitPir_expression_list(self, ctx:like_rubyParser.Pir_expression_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition.
  def visitFunction_definition(self, ctx:like_rubyParser.Function_definitionContext):
    if ctx.function_definition_header().function_name().id_function() == None:
        function_name = str(ctx.function_definition_header().function_name().my_id().ID())
    else:
        function_name = str(ctx.function_definition_header().function_name().id_function().ID())
    if ctx in self.programm.expressions:
        self.programm.remove_expression(ctx)
        if (not function_name in self.programm.declared_function_names) or (function_name in self.programm.local_variables):
            self.programm.errors.append("Hello function name error")
        else:
            function = AstFunction(function_name)
            self.programm.functions.append(function)
            self.function = function
            function.expressions.append(ctx.function_definition_body())
            self.programm.defined_function_names.append(function_name)
            function.function_params.append(ctx.function_definition_header().function_definition_params())
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_body.
  def visitFunction_definition_body(self, ctx:like_rubyParser.Function_definition_bodyContext):
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                func.expressions.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_header.
  def visitFunction_definition_header(self, ctx:like_rubyParser.Function_definition_headerContext):
    if ctx in self.programm.declared_function_names:
        self.programm.declared_function_names.remove(ctx)
        if ctx.function_name().id_function() == None:
            function_name = str(ctx.function_name().my_id().ID())
        else:
            function_name = str(ctx.function_name().id_function().ID())
        if function_name in self.programm.declared_function_names:
            self.programm.errors.append("Hello function declaretion error")
        else:
            self.programm.declared_function_names.append(function_name)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_name.
  def visitFunction_name(self, ctx):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_params.
  def visitFunction_definition_params(self, ctx:like_rubyParser.Function_definition_paramsContext):
    for func in self.programm.functions:
        if ctx in func.function_params:
            func.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    func.function_params.append(child)
    for table in self.table_assignments:
        if ctx in table.columns:
            table.columns.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    table.columns.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_params_list.
  def visitFunction_definition_params_list(self, ctx:like_rubyParser.Function_definition_params_listContext):
    #for function in self.programm.functions:
    for func in self.programm.functions:
        if ctx in func.function_params:
            func.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    func.function_params.append(child)
    for table in self.table_assignments:
        if ctx in table.columns:
            table.columns.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    table.columns.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_param_id.
  def visitFunction_definition_param_id(self, ctx:like_rubyParser.Function_definition_param_idContext):
    for func in self.programm.functions:
        if ctx in func.function_params:
            func.function_params.remove(ctx)
            func.function_params.append(str(ctx.my_id().ID()))
    for table in self.table_assignments:
        if ctx in table.columns:
            table.columns.remove(ctx)
            if str(ctx.my_id().ID()) in self.programm.local_variables:
                table.columns.append(str(ctx.my_id().ID()))
            else:
                error = "Hello table assignment params error"
                self.programm.errors.append(error)

            print(table.columns)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#return_statement.
  def visitReturn_statement(self, ctx:like_rubyParser.Return_statementContext):
    return self.visitChildren(ctx)

  #TODO check calling function in params of function!!!
  # Visit a parse tree produced by like_rubyParser#function_call.
  def visitFunction_call(self, ctx:like_rubyParser.Function_callContext):
    function_name = str(ctx.function_name().my_id().ID())
    calling = AstFunctionCall()
    self.function_calls.append(calling)
    calling.name = function_name
    if not function_name in self.programm.declared_function_names:
        error_text = "Hello function_call error: " + function_name # if function defined after function call this error will also occur
        self.programm.errors.append(error_text)
    else:
        for func in self.programm.functions:
            if ctx in func.expressions:
                func.expressions.remove(ctx)
                func.expressions.append(calling)
                for child in ctx.children:
                    if child.__class__.__name__ == "Function_call_param_listContext":
                        calling.function_params.append(child)
        for func in self.for_statement:
            if ctx in func.expressions:
                func.expressions.remove(ctx)
                func.expressions.append(calling)
                for child in ctx.children:
                    if child.__class__.__name__ == "Function_call_param_listContext":
                        calling.function_params.append(child)
        for assignment in self.row_assignments:
            if ctx in assignment.table:
                assignment.table.remove(ctx)
                assignment.table.append(calling)
                for child in ctx.children:
                    if child.__class__.__name__ == "Function_call_param_listContext":
                        calling.function_params.append(child)
        for func in self.if_statements:
            if ctx in func.if_expressions:
                func.if_expressions.remove(ctx)
                func.if_expressions.append(calling)
                for child in ctx.children:
                    if child.__class__.__name__ == "Function_call_param_listContext":
                        calling.function_params.append(child)
            if ctx in func.else_expressions:
                func.else_expressions.remove(ctx)
                func.else_expressions.append(calling)
                for child in ctx.children:
                    if child.__class__.__name__ == "Function_call_param_listContext":
                        calling.function_params.append(child)
        if ctx in self.programm.expressions:
            self.programm.expressions.remove(ctx)
            self.programm.expressions.append(calling)
            for child in ctx.children:
                if child.__class__.__name__ == "Function_call_param_listContext":
                    calling.function_params.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_param_list.
  def visitFunction_call_param_list(self, ctx:like_rubyParser.Function_call_param_listContext):
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                call.function_params.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_params.
  def visitFunction_call_params(self, ctx:like_rubyParser.Function_call_paramsContext):
    for call in self.function_calls:
        if ctx in call.function_params:
              call.function_params.remove(ctx)
              for child in ctx.children:
                  if child.__class__.__name__ != 'TerminalNodeImpl':
                      call.function_params.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_param.
  def visitFunction_param(self, ctx:like_rubyParser.Function_paramContext):
    for call in self.function_calls:
        if ctx in call.function_params:
              call.function_params.remove(ctx)
              for child in ctx.children:
                  if child.__class__.__name__ != 'TerminalNodeImpl':
                      call.function_params.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_unnamed_param.
  def visitFunction_unnamed_param(self, ctx:like_rubyParser.Function_unnamed_paramContext):
    for call in self.function_calls:
        if ctx in call.function_params:
              call.function_params.remove(ctx)
              for child in ctx.children:
                  if child.__class__.__name__ != 'TerminalNodeImpl':
                      call.function_params.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_named_param.
  def visitFunction_named_param(self, ctx:like_rubyParser.Function_named_paramContext):

    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_assignment.
  def visitFunction_call_assignment(self, ctx:like_rubyParser.Function_call_assignmentContext):
    for assignment in self.row_assignments:
        if ctx in assignment.table:
            assignment.table.remove(ctx)
            for child in ctx.children:
                assignment.table.append(child)
        print("AKJSBFJKSABLAJLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
        assignment.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#all_result.
  def visitAll_result(self, ctx:like_rubyParser.All_resultContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.end_value.append(str(child))
                else:
                    stat.end_value.append(child)
    for stat in self.if_statements:
        if ctx in stat.condition:
            stat.condition.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.condition.append(str(child))
                else:
                    stat.condition.append(child)
        if ctx in stat.var:
            stat.var.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.var.append(str(child))
                else:
                    stat.var.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#elsif_statement.
  def visitElsif_statement(self, ctx:like_rubyParser.Elsif_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#if_elsif_statement.
  def visitIf_elsif_statement(self, ctx:like_rubyParser.If_elsif_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#if_statement.
  def visitIf_statement(self, ctx:like_rubyParser.If_statementContext):
    if_statement = AstIfStatement()
    self.if_statements.append(if_statement)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            func.expressions.append(if_statement)
            for child in ctx.children:
                if_statement.condition.append(child)
            return self.visitChildren(ctx)
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        self.programm.expressions.append(if_statement)
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminalNodeImpl':
                if_statement.condition.append(child)
            if child.__class__.__name__ == 'Statement_bodyContext':
                if len(if_statement.if_expressions) == 0:
                    if_statement.if_expressions.append(child)
                else:
                    if_statement.else_expressions.append(child)
                if_statement.condition.remove(child)
            if child.__class__.__name__ == 'Cond_expressionContext':
                if_statement.condition.remove(child)
                if_statement.condition.append(ctx.cond_expression().comparison_list())
            if child.__class__.__name__ == 'CrlfContext' or child.__class__.__name__ == 'Else_tokenContext':
                if_statement.condition.remove(child)
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #if_statement.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#unless_statement.
  def visitUnless_statement(self, ctx:like_rubyParser.Unless_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#while_statement.
  def visitWhile_statement(self, ctx:like_rubyParser.While_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_statement.
  def visitFor_statement(self, ctx:like_rubyParser.For_statementContext):
    for_statement = AstForStatement()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        self.programm.expressions.append(for_statement)
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminalNodeImpl':
                for_statement.start_value.append(child)
            if child.__class__.__name__ == 'Statement_bodyContext':
                for_statement.expressions.append(ctx.statement_body().statement_expression_list())
                for_statement.start_value.remove(child)
            if child.__class__.__name__ == 'Cond_expressionContext':
                for comp in ctx.cond_expression().comparison_list().children:
                    for_statement.end_value.append(comp)
                    for_statement.start_value.remove(child)
            if child.__class__.__name__ == 'Loop_expressionContext':
                for_statement.end_value.append(child)
                for_statement.start_value.remove(child)
            if child.__class__.__name__ == 'CrlfContext':
                for_statement.start_value.remove(child)
    self.for_statement.append(for_statement)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#init_expression.
  def visitInit_expression(self, ctx:like_rubyParser.Init_expressionContext):
    for stat in self.for_statement:
        if ctx in stat.start_value:
            stat.start_value.remove(ctx)
            for child in ctx.children:
                stat.start_value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#all_assignment.
  def visitAll_assignment(self, ctx:like_rubyParser.All_assignmentContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                stat.end_value.append(child)
    #for stat in self.if_statements:
        #if ctx in stat.condition:
            #stat.condition.remove(ctx)
            #for child in ctx.children:
                #stat.condition.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_init_list.
  def visitFor_init_list(self, ctx:like_rubyParser.For_init_listContext):
    for stat in self.for_statement:
        if ctx in stat.start_value:
            stat.start_value.remove(ctx)
            stat.start_value.append(ctx.all_assignment().children[0])
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#cond_expression.
  def visitCond_expression(self, ctx:like_rubyParser.Cond_expressionContext):

    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#loop_expression.
  def visitLoop_expression(self, ctx:like_rubyParser.Loop_expressionContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                stat.end_value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_loop_list.
  def visitFor_loop_list(self, ctx:like_rubyParser.For_loop_listContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                stat.end_value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#statement_body.
  def visitStatement_body(self, ctx:like_rubyParser.Statement_bodyContext):
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            stat.if_expressions.remove(ctx)
            for child in ctx.children:
                stat.if_expressions.append(child)
        if ctx in stat.else_expressions:
            stat.else_expressions.remove(ctx)
            for child in ctx.children:
                stat.else_expressions.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#statement_expression_list.
  def visitStatement_expression_list(self, ctx:like_rubyParser.Statement_expression_listContext):
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.expressions.append(child)
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            stat.if_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.if_expressions.append(child)
        if ctx in stat.else_expressions:
            stat.else_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.else_expressions.append(child)
        #print("LASJFBKJABFLSABFLASB___________")
        #stat.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#dynamic_assignment.
  def visitDynamic_assignment(self, ctx:like_rubyParser.Dynamic_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#int_assignment.
  def visitInt_assignment(self, ctx:like_rubyParser.Int_assignmentContext):
    int_assignment = AstIntAssignment()
    self.int_assignments.append(int_assignment)
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    int_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    int_assignment.value.append(child)
        self.programm.expressions.append(int_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx. children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        int_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in int_assignment.value:
                            int_assignment.value.append(child)
            func.expressions.append(int_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        int_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        int_assignment.value.append(child)
            call.function_params.append(int_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    if child.__class__.__name__ == "LvalueContext":
                        int_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in int_assignment.value:
                            int_assignment.value.append(child)
            stat.expression.append(int_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#float_assignment.
  def visitFloat_assignment(self, ctx:like_rubyParser.Float_assignmentContext):
    float_assignment = AstFloatAssignment()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    float_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    float_assignment.value.append(child)
        self.programm.expressions.append(float_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        float_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in float_assignment.value:
                            float_assignment.value.append(child)
            func.expressions.append(float_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        float_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        float_assignment.value.append(child)
            call.function_params.append(float_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    if child.__class__.__name__ == "LvalueContext":
                        float_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in float_assignment.value:
                            float_assignment.value.append(child)
            stat.expression.append(float_assignment)
    self.float_assignments.append(float_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#string_assignment.
  def visitString_assignment(self, ctx:like_rubyParser.String_assignmentContext):
    string_assignment = AstStringAssignment()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    string_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    string_assignment.value.append(child)
        self.programm.expressions.append(string_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.value:
                            string_assignment.value.append(child)
            func.expressions.append(string_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        string_assignment.value.append(child)
            call.function_params.append(string_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        string_assignment.value.append(child)
            stat.expressions.append(string_assignment)
    self.string_assignments.append(string_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#table_assignment.
  def visitTable_assignment(self, ctx:like_rubyParser.Table_assignmentContext):
    string_assignment = AstTableAssignment()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    string_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    string_assignment.columns.append(child)
        self.programm.expressions.append(string_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.columns:
                            string_assignment.columns.append(child)
            func.expressions.append(string_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        string_assignment.value.append(child)
            call.function_params.append(string_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.value:
                            string_assignment.value.append(child)
            stat.expression.append(string_assignment)
    self.table_assignments.append(string_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#column_assignment.
  def visitColumn_assignment(self, ctx:like_rubyParser.Column_assignmentContext):
    string_assignment = AstColumnAssignment()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    string_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    string_assignment.params.append(child)
        self.programm.expressions.append(string_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.params:
                            string_assignment.params.append(child)
            func.expressions.append(string_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        string_assignment.value.append(child)
            call.function_params.append(string_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.value:
                            string_assignment.value.append(child)
            stat.expression.append(string_assignment)
    self.column_assignments.append(string_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#row_assignment.
  def visitRow_assignment(self, ctx:like_rubyParser.Row_assignmentContext):
    string_assignment = AstRowAssignment()
    if ctx in self.programm.expressions:
        self.programm.expressions.remove(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != "TerminalNodeImpl":
                if child.__class__.__name__ == "LvalueContext":
                    string_assignment.var = ctx.lvalue().my_id().ID()
                else:
                    string_assignment.params.append(child)
        self.programm.expressions.append(string_assignment)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.params:
                            string_assignment.params.append(child)
            func.expressions.append(string_assignment)
    for call in self.function_calls:
        if ctx in call.function_params:
            call.function_params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        string_assignment.value.append(child)
            call.function_params.append(string_assignment)
    for stat in self.for_statement:
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    if child.__class__.__name__ == "LvalueContext":
                        string_assignment.var = ctx.lvalue().my_id().ID()
                    else:
                        if not child in string_assignment.value:
                            string_assignment.value.append(child)
            stat.expression.append(string_assignment)
    self.row_assignments.append(string_assignment)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#assignment.
  def visitAssignment(self, ctx:like_rubyParser.AssignmentContext):
    for stat in self.for_statement:
        if ctx in stat.start_value:
            stat.start_value.remove(ctx)
            for child in ctx.children:
                stat.start_value.append(child)
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    stat.end_value.append(child)
                else:
                    stat.end_value.append(str(child))
        if ctx in stat.expressions:
            assignment = AstVariable()
            stat.expressions.remove(ctx)
            stat.expressions.append(assignment)
            self.assignments.append(assignment)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    assignment.value.append(child)
                else:
                    assignment.value.append(str(child))
                    if str(child) == '=' or str(child) == '+=' or str(child) == '-=' or str(child) == '*=' or str(child) == '/=':
                        assignment.operator = (str(child))
                        assignment.value.remove(str(child))
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            assignment = AstVariable()
            stat.if_expressions.remove(ctx)
            stat.if_expressions.append(assignment)
            self.assignments.append(assignment)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    assignment.value.append(child)
                else:
                    assignment.value.append(str(child))
                    if str(child) == '=' or str(child) == '+=' or str(child) == '-=' or str(child) == '*=' or str(child) == '/=':
                        assignment.operator = (str(child))
                        assignment.value.remove(str(child))
        if ctx in stat.else_expressions:
            assignment = AstVariable()
            stat.else_expressions.remove(ctx)
            stat.else_expressions.append(assignment)
            self.assignments.append(assignment)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    assignment.value.append(child)
                else:
                    assignment.value.append(str(child))
                    if str(child) == '=' or str(child) == '+=' or str(child) == '-=' or str(child) == '*=' or str(child) == '/=':
                        assignment.operator = (str(child))
                        assignment.value.remove(str(child))
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#initial_array_assignment.
  def visitInitial_array_assignment(self, ctx:like_rubyParser.Initial_array_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#array_assignment.
  def visitArray_assignment(self, ctx:like_rubyParser.Array_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#array_definition.
  def visitArray_definition(self, ctx:like_rubyParser.Array_definitionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#array_definition_elements.
  def visitArray_definition_elements(self, ctx:like_rubyParser.Array_definition_elementsContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#array_selector.
  def visitArray_selector(self, ctx:like_rubyParser.Array_selectorContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#dynamic_result.
  def visitDynamic_result(self, ctx:like_rubyParser.Dynamic_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#dynamic.
  def visitDynamic(self, ctx:like_rubyParser.DynamicContext):
    for call in self.function_calls:
        if ctx in call.function_params:
              call.function_params.remove(ctx)
              for child in ctx.children:
                  if child.__class__.__name__ != 'TerminalNodeImpl':
                      call.function_params.append(str(ctx.my_id().ID()))
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminalNodeImpl':
                    stat.end_value.append(str(ctx.my_id().ID()))
    for stat in self.if_statements:
        if ctx in stat.var:
            stat.var.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminalNodeImpl':
                    stat.var.append(str(ctx.my_id().ID()))
        print("LASJFBKJABFLSABFLASB___________")
        stat.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#int_result.
  def visitInt_result(self, ctx:like_rubyParser.Int_resultContext):
    for assignment in self.int_assignments:
        if ctx in assignment.value:
            assignment.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assignment.value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        assignment.value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            assignment.value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                assignment.value.append(str(child.FLOAT()))
                            else:
                                assignment.value.append(child)
    for call in self.function_calls:
        if ctx in call.function_params:
              call.function_params.remove(ctx)
              for child in ctx.children:
                  if child.__class__.__name__ != 'TerminalNodeImpl':
                      call.function_params.append(child)
    for assign in self.assignments:
        if ctx in assign.value:
            assign.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assign.value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        assign.value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            assign.value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                assign.value.append(str(child.FLOAT()))
                            else:
                                assign.value.append(child)
    for stat in self.for_statement:
        if ctx in stat.start_value:
            stat.start_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    stat.start_value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        stat.start_value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            stat.start_value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                stat.start_value.append(str(child.FLOAT()))
                            else:
                                stat.start_value.append(child)
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    stat.end_value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        stat.end_value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            stat.end_value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                stat.end_value.append(str(child.FLOAT()))
                            else:
                                stat.end_value.append(child)
    for stat in self.if_statements:
        if ctx in stat.var:
            stat.var.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    stat.var.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        stat.var.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            stat.var.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                stat.var.append(str(child.FLOAT()))
                            else:
                                stat.var.append(child)
        if ctx in stat.condition:
            stat.condition.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    stat.condition.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        stat.condition.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            stat.condition.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                stat.condition.append(str(child.FLOAT()))
                            else:
                                stat.condition.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#float_result.
  def visitFloat_result(self, ctx:like_rubyParser.Float_resultContext):
    for assignment in self.float_assignments:
        if ctx in assignment.value:
            assignment.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assignment.value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        assignment.value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            assignment.value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                assignment.value.append(str(child.FLOAT()))
                            else:
                                assignment.value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#string_result.
  def visitString_result(self, ctx:like_rubyParser.String_resultContext):
    for assignment in self.string_assignments:
        if ctx in assignment.value:
            assignment.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assignment.value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        assignment.value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            assignment.value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                assignment.value.append(str(child.FLOAT()))
                            else:
                                assignment.value.append(child)
    for assign in self.assignments:
        if ctx in assign.value:
            assign.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assign.value.append(str(child))
                else:
                    if child.__class__.__name__ == "Literal_tContext":
                        assign.value.append(str(child.LITERAL()))
                    else:
                        if child.__class__.__name__ == "Int_tContext":
                            assign.value.append(str(child.INT()))
                        else:
                            if child.__class__.__name__ == "Float_tContext":
                                assign.value.append(str(child.FLOAT()))
                            else:
                                assign.value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#table_result.
  def visitTable_result(self, ctx:like_rubyParser.Table_resultContext):
    for assignment in self.table_assignments:
        if ctx in assignment.columns:
            assignment.columns.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    assignment.columns.append(str(child))
                else:
                    for child_child in child.children:
                        if child_child.__class__.__name__ == "TerminalNodeImpl":
                            assignment.columns.append(str(child_child))
                        if child_child.__class__.__name__ =='Function_definition_params_listContext':
                            assignment.columns.append(child_child)
        assignment.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#column_result.
  def visitColumn_result(self, ctx:like_rubyParser.Column_resultContext):
    for assignment in self.column_assignments:
        if ctx in assignment.params:
            assignment.params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ == "TerminalNodeImpl":
                    if str(child) == "Integer" or str(child) == "String" or str(child) == "Float":
                        assignment.type = str(child)
                    else:
                        assignment.params.append(str(child))
                if child.__class__.__name__ =='Literal_tContext':
                    assignment.column_name = (str(child.LITERAL()))
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#row_result.
  def visitRow_result(self, ctx:like_rubyParser.Row_resultContext):
    for assignment in self.row_assignments:
        if ctx in assignment.params:
            assignment.params.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='My_idContext':
                    assignment.row_vars = (str(child.ID()))
                if child.__class__.__name__ =='Function_call_assignmentContext':
                    assignment.table.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comparison_list.
  def visitComparison_list(self, ctx:like_rubyParser.Comparison_listContext):
    for stat in self.if_statements:
        if ctx in stat.condition:
            stat.condition.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.condition.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comparison.
  def visitComparison(self, ctx:like_rubyParser.ComparisonContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.end_value.append(str(child))
                else:
                    stat.end_value.append(child)
    for stat in self.if_statements:
        if ctx in stat.condition:
            stat.condition.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.operator = (str(child))
                else:
                    stat.condition.append(child)
            print(len(stat.condition))
            value = stat.condition[-2]
            stat.condition.remove(value)
            stat.var.append(value)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comp_var.
  def visitComp_var(self, ctx:like_rubyParser.Comp_varContext):
    for stat in self.for_statement:
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.end_value.append(str(child))
                else:
                    stat.end_value.append(child)
    for stat in self.if_statements:
        if ctx in stat.condition:
            stat.condition.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.condition.append(str(child))
                else:
                    stat.condition.append(child)
        if ctx in stat.var:
            stat.var.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ =='TerminalNodeImpl':
                    stat.var.append(str(child))
                else:
                    stat.var.append(child)
        print("LASJFBKJABFLSABFLASB___________")
        stat.print_info()
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#lvalue.
  def visitLvalue(self, ctx:like_rubyParser.LvalueContext):
     var_name = ctx.my_id().ID()
     if var_name in self.programm.local_variables or var_name in self.programm.declared_function_names:
         self.programm.errors.append("Hello local_values error")
     else:
         self.programm.local_variables.append(str(var_name))
     for stat in self.for_statement:
         if ctx in stat.start_value:
             stat.start_value.remove(ctx)
             for child in ctx.children:
                 if child.__class__.__name__ != 'TerminatorContext':
                     stat.var = (str(child.ID()))
         if ctx in stat.end_value:
             stat.end_value.remove(ctx)
             for child in ctx.children:
                 if child.__class__.__name__ != 'TerminatorContext':
                     stat.end_value.append(str(child.ID()))
     for assign in self.assignments:
         if ctx in assign.value:
             assign.value.remove(ctx)
             for child in ctx.children:
                 if child.__class__.__name__ != "TerminalNodeImpl":
                     assign.name = var_name
     return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#rvalue.
  def visitRvalue(self, ctx:like_rubyParser.RvalueContext):
    if ctx in self.programm.expressions:
        self.programm.remove_expression(ctx)
        for child in ctx.children:
            if child.__class__.__name__ != 'TerminatorContext':
                self.programm.add_expression(child)
    for func in self.programm.functions:
        if ctx in func.expressions:
            func.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    func.expressions.append(child)
    for stat in self.for_statement:
        if ctx in stat.start_value:
            stat.start_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.start_value.append(child)
        if ctx in stat.end_value:
            stat.end_value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    stat.end_value.append(child)
        if ctx in stat.expressions:
            stat.expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    stat.expressions.append(child)
    for stat in self.if_statements:
        if ctx in stat.if_expressions:
            stat.if_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    stat.if_expressions.append(child)
        if ctx in stat.else_expressions:
            stat.else_expressions.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    stat.else_expressions.append(child)
        print("-----------------------------------------000000000")
        stat.print_info()
    for assign in self.assignments:
        if ctx in assign.value:
            assign.value.remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != "TerminalNodeImpl":
                    assign.value.append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#break_expression.
  def visitBreak_expression(self, ctx:like_rubyParser.Break_expressionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#literal_t.
  def visitLiteral_t(self, ctx:like_rubyParser.Literal_tContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#float_t.
  def visitFloat_t(self, ctx:like_rubyParser.Float_tContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#int_t.
  def visitInt_t(self, ctx:like_rubyParser.Int_tContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#bool_t.
  def visitBool_t(self, ctx:like_rubyParser.Bool_tContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#nil_t.
  def visitNil_t(self, ctx:like_rubyParser.Nil_tContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#my_id.
  def visitMy_id(self, ctx:like_rubyParser.My_idContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#id_global.
  def visitId_global(self, ctx:like_rubyParser.Id_globalContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#id_function.
  def visitId_function(self, ctx:like_rubyParser.Id_functionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#terminator.
  def visitTerminator(self, ctx:like_rubyParser.TerminatorContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#else_token.
  def visitElse_token(self, ctx:like_rubyParser.Else_tokenContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#crlf.
  def visitCrlf(self, ctx:like_rubyParser.CrlfContext):
    return self.visitChildren(ctx)
