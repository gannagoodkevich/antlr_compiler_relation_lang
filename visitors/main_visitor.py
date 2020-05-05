import copy
import re

from like_rubyVisitor import like_rubyVisitor
# from visitors.value_visitor import ValueVisitor
# from visitors.function_visitor import FunctionVisitio
from like_rubyLexer import like_rubyLexer
from like_rubyParser import like_rubyParser
from namespace import Namespace


class Visitor(like_rubyVisitor):
  def __init__(self):
    #self.namespace = copy.deepcopy(namespace) or Namespace()
    #for local in list(locals_):
    #  self.namespace.add_var(local.name, local.type)
    #self.block = Block()
    self.memory = {}
    self.memory['local_values'] = []
    self.memory['defined_function_name'] = []
    self.memory['declared_function_name'] = []
    self.memory['errors'] = []
    #self.file = file
    #self.file.write("Start working with visitor\n")
    self.assignment = 0
    self.body_of_function = 0

  # Visit a parse tree produced by like_rubyParser#prog.
  def visitProg(self, ctx:like_rubyParser.ProgContext):
    print("I'm in visit Prog")
    return self.visitChildren(ctx)
    #for statement in ctx.statement():
      # self.block.add_statement(self.visitStatement(statement))
    #  print(statement)
    #  print("--->")



  # Visit a parse tree produced by like_rubyParser#function_definition_list.
  def visitFunction_definition_list(self, ctx:like_rubyParser.Function_definition_listContext):
    if ctx.function_definition_header().function_name().id_function() == None:
        function_name = str(ctx.function_definition_header().function_name().my_id().ID())
    else:
        function_name = str(ctx.function_definition_header().function_name().id_function().ID())
    if function_name in self.memory['declared_function_name']:
        self.memory["errors"].append("Function decclaretion error")
    else:
        self.memory['declared_function_name'].append(function_name)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#expression_list.
  def visitExpression_list(self, ctx:like_rubyParser.Expression_listContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            for child in ctx.children:
                if child.__class__.__name__ != 'TerminatorContext':
                    self.memory["func1_body"][1]["expressions"].append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#expression.
  def visitExpression(self, ctx:like_rubyParser.ExpressionContext):
    #print(str(ctx))
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            #print("visitexpression")
        #    print("hello func context")
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            for child in ctx.children:
                self.memory["func1_body"][1]["expressions"].append(child)
            #if ctx.function_definition() != None:
            #    self.memory["func1_body"].append(ctx.function_definition())
            #if ctx.function_inline_call() != None:
            #    self.memory["func1_body"].append(ctx.function_inline_call())
            #if ctx.require_block() != None:
            #    self.memory["func1_body"].append(ctx.require_block())
            #if ctx.if_statement() != None:
            #    self.memory["func1_body"].append(ctx.if_statement())
            #if ctx.unless_statement() != None:
            #    self.memory["func1_body"].append(ctx.unless_statement())
            #if ctx.rvalue() != None:
            #    self.memory["func1_body"].append(ctx.rvalue())
            #if ctx.return_statement() != None:
            #    self.memory["func1_body"].append(ctx.return_statement())
            #if ctx.while_statement() != None:
            #    self.memory["func1_body"].append(ctx.while_statement())
            #if ctx.for_statement() != None:
            #    self.memory["func1_body"].append(ctx.for_statement())
            #if ctx.pir_inline() != None:
            #    self.memory["func1_body"].append(ctx.pir_inline())
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
    if function_name in self.memory['declared_function_name']:
        print("Okey, captain!")
    else:
        self.memory["errors"].append("Function definition error: declare this function!")
    if function_name in self.memory['defined_function_name']:
        self.memory["errors"].append("Hello function_name error")
    else:
        if function_name in self.memory['local_values']:
            self.memory["errors"].append("Hello function_name error: there is local_value with the same name")
        else:
            self.memory['defined_function_name'].append(function_name)
    if ctx.function_definition_body() != None:
        body_name = function_name + "_body"
        self.memory[body_name] = []
        #print(str(ctx.function_definition_body().expression_list().expression()))
        self.memory[body_name].append(ctx.function_definition_body())
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_body.
  def visitFunction_definition_body(self, ctx:like_rubyParser.Function_definition_bodyContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"]:
            self.memory["func1_body"].append({"expressions": ctx.children})
            print(ctx.children)
    self.memory["func1_body"].append({"func1_variables": []})
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_header.
  def visitFunction_definition_header(self, ctx:like_rubyParser.Function_definition_headerContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_name.
  def visitFunction_name(self, ctx):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_params.
  def visitFunction_definition_params(self, ctx:like_rubyParser.Function_definition_paramsContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_params_list.
  def visitFunction_definition_params_list(self, ctx:like_rubyParser.Function_definition_params_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_definition_param_id.
  def visitFunction_definition_param_id(self, ctx:like_rubyParser.Function_definition_param_idContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#return_statement.
  def visitReturn_statement(self, ctx:like_rubyParser.Return_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call.
  def visitFunction_call(self, ctx:like_rubyParser.Function_callContext):
    function_name = str(ctx.function_name().my_id().ID())
    if not function_name in self.memory['defined_function_name']:
        self.memory["errors"].append("Hello function_call error")
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_param_list.
  def visitFunction_call_param_list(self, ctx:like_rubyParser.Function_call_param_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_params.
  def visitFunction_call_params(self, ctx:like_rubyParser.Function_call_paramsContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_param.
  def visitFunction_param(self, ctx:like_rubyParser.Function_paramContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_unnamed_param.
  def visitFunction_unnamed_param(self, ctx:like_rubyParser.Function_unnamed_paramContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_named_param.
  def visitFunction_named_param(self, ctx:like_rubyParser.Function_named_paramContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#function_call_assignment.
  def visitFunction_call_assignment(self, ctx:like_rubyParser.Function_call_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#all_result.
  def visitAll_result(self, ctx:like_rubyParser.All_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#elsif_statement.
  def visitElsif_statement(self, ctx:like_rubyParser.Elsif_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#if_elsif_statement.
  def visitIf_elsif_statement(self, ctx:like_rubyParser.If_elsif_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#if_statement.
  def visitIf_statement(self, ctx:like_rubyParser.If_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#unless_statement.
  def visitUnless_statement(self, ctx:like_rubyParser.Unless_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#while_statement.
  def visitWhile_statement(self, ctx:like_rubyParser.While_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_statement.
  def visitFor_statement(self, ctx:like_rubyParser.For_statementContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#init_expression.
  def visitInit_expression(self, ctx:like_rubyParser.Init_expressionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#all_assignment.
  def visitAll_assignment(self, ctx:like_rubyParser.All_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_init_list.
  def visitFor_init_list(self, ctx:like_rubyParser.For_init_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#cond_expression.
  def visitCond_expression(self, ctx:like_rubyParser.Cond_expressionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#loop_expression.
  def visitLoop_expression(self, ctx:like_rubyParser.Loop_expressionContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#for_loop_list.
  def visitFor_loop_list(self, ctx:like_rubyParser.For_loop_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#statement_body.
  def visitStatement_body(self, ctx:like_rubyParser.Statement_bodyContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#statement_expression_list.
  def visitStatement_expression_list(self, ctx:like_rubyParser.Statement_expression_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#dynamic_assignment.
  def visitDynamic_assignment(self, ctx:like_rubyParser.Dynamic_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#int_assignment.
  def visitInt_assignment(self, ctx:like_rubyParser.Int_assignmentContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            self.assignment = "int_assignment_" + str(id(ctx))
            self.memory["func1_body"][1]["expressions"].append({self.assignment: []})
            for exp in self.memory["func1_body"][1]["expressions"]:
                if exp.__class__.__name__ == "dict" and self.assignment in exp:
                    for child in ctx.children:
                        if child.__class__.__name__ == "TerminalNodeImpl":
                            exp[self.assignment].append(str(child))
                        else:
                            exp[self.assignment].append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#float_assignment.
  def visitFloat_assignment(self, ctx:like_rubyParser.Float_assignmentContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            self.assignment = "float_assignment_" + str(id(ctx))
            self.memory["func1_body"][1]["expressions"].append({self.assignment: []})
            for exp in self.memory["func1_body"][1]["expressions"]:
                if exp.__class__.__name__ == "dict" and self.assignment in exp:
                    for child in ctx.children:
                        if child.__class__.__name__ == "TerminalNodeImpl":
                            exp[self.assignment].append(str(child))
                        else:
                            exp[self.assignment].append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#string_assignment.
  def visitString_assignment(self, ctx:like_rubyParser.String_assignmentContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            self.assignment = "float_assignment_" + str(id(ctx))
            self.memory["func1_body"][1]["expressions"].append({self.assignment: []})
            for exp in self.memory["func1_body"][1]["expressions"]:
                if exp.__class__.__name__ == "dict" and self.assignment in exp:
                    for child in ctx.children:
                        if child.__class__.__name__ == "TerminalNodeImpl":
                            exp[self.assignment].append(str(child))
                        else:
                            exp[self.assignment].append(child)
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#table_assignment.
  def visitTable_assignment(self, ctx:like_rubyParser.Table_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#column_assignment.
  def visitColumn_assignment(self, ctx:like_rubyParser.Column_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#row_assignment.
  def visitRow_assignment(self, ctx:like_rubyParser.Row_assignmentContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#assignment.
  def visitAssignment(self, ctx:like_rubyParser.AssignmentContext):
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
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#int_result.
  def visitInt_result(self, ctx:like_rubyParser.Int_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#float_result.
  def visitFloat_result(self, ctx:like_rubyParser.Float_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#string_result.
  def visitString_result(self, ctx:like_rubyParser.String_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#table_result.
  def visitTable_result(self, ctx:like_rubyParser.Table_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#column_result.
  def visitColumn_result(self, ctx:like_rubyParser.Column_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#row_result.
  def visitRow_result(self, ctx:like_rubyParser.Row_resultContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comparison_list.
  def visitComparison_list(self, ctx:like_rubyParser.Comparison_listContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comparison.
  def visitComparison(self, ctx:like_rubyParser.ComparisonContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#comp_var.
  def visitComp_var(self, ctx:like_rubyParser.Comp_varContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#lvalue.
  def visitLvalue(self, ctx:like_rubyParser.LvalueContext):
     var_name = ctx.my_id().ID()
     if "func1_body" in self.memory:
         for exp in self.memory["func1_body"][1]["expressions"]:
             if exp.__class__.__name__ == "dict" and self.assignment in exp and ctx in exp[self.assignment]:
                 exp[self.assignment].remove(ctx)
                 if str(var_name) in self.memory['defined_function_name']:
                     self.memory["errors"].append("Hello local_values error: there is function with the same name")
                 else:
                     exp[self.assignment].append(str(var_name))
                     self.memory["func1_body"][2]["func1_variables"].append(str(var_name))
     else:
        if str(var_name) in self.memory['local_values']:
            self.memory["errors"].append("Hello local_values error")
        else:
            if str(var_name) in self.memory['defined_function_name']:
                self.memory["errors"].append("Hello local_values error: there is function with the same name")
            else:
                self.memory['local_values'].append(str(var_name))
     return self.visitChildren(ctx)


  # Visit a parse tree produced by like_rubyParser#rvalue.
  def visitRvalue(self, ctx:like_rubyParser.RvalueContext):
    if "func1_body" in self.memory:
        if ctx in self.memory["func1_body"][1]["expressions"]:
            self.memory["func1_body"][1]["expressions"].remove(ctx)
            for child in ctx.children:
                self.memory["func1_body"][1]["expressions"].append(child)
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
