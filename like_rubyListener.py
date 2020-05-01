# Generated from like_ruby.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .like_rubyParser import like_rubyParser
else:
    from like_rubyParser import like_rubyParser

# This class defines a complete listener for a parse tree produced by like_rubyParser.
class like_rubyListener(ParseTreeListener):

    # Enter a parse tree produced by like_rubyParser#prog.
    def enterProg(self, ctx:like_rubyParser.ProgContext):
        pass

    # Exit a parse tree produced by like_rubyParser#prog.
    def exitProg(self, ctx:like_rubyParser.ProgContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_list.
    def enterFunction_definition_list(self, ctx:like_rubyParser.Function_definition_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_list.
    def exitFunction_definition_list(self, ctx:like_rubyParser.Function_definition_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#expression_list.
    def enterExpression_list(self, ctx:like_rubyParser.Expression_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#expression_list.
    def exitExpression_list(self, ctx:like_rubyParser.Expression_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#expression.
    def enterExpression(self, ctx:like_rubyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#expression.
    def exitExpression(self, ctx:like_rubyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#global_get.
    def enterGlobal_get(self, ctx:like_rubyParser.Global_getContext):
        pass

    # Exit a parse tree produced by like_rubyParser#global_get.
    def exitGlobal_get(self, ctx:like_rubyParser.Global_getContext):
        pass


    # Enter a parse tree produced by like_rubyParser#global_set.
    def enterGlobal_set(self, ctx:like_rubyParser.Global_setContext):
        pass

    # Exit a parse tree produced by like_rubyParser#global_set.
    def exitGlobal_set(self, ctx:like_rubyParser.Global_setContext):
        pass


    # Enter a parse tree produced by like_rubyParser#global_result.
    def enterGlobal_result(self, ctx:like_rubyParser.Global_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#global_result.
    def exitGlobal_result(self, ctx:like_rubyParser.Global_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_inline_call.
    def enterFunction_inline_call(self, ctx:like_rubyParser.Function_inline_callContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_inline_call.
    def exitFunction_inline_call(self, ctx:like_rubyParser.Function_inline_callContext):
        pass


    # Enter a parse tree produced by like_rubyParser#require_block.
    def enterRequire_block(self, ctx:like_rubyParser.Require_blockContext):
        pass

    # Exit a parse tree produced by like_rubyParser#require_block.
    def exitRequire_block(self, ctx:like_rubyParser.Require_blockContext):
        pass


    # Enter a parse tree produced by like_rubyParser#pir_inline.
    def enterPir_inline(self, ctx:like_rubyParser.Pir_inlineContext):
        pass

    # Exit a parse tree produced by like_rubyParser#pir_inline.
    def exitPir_inline(self, ctx:like_rubyParser.Pir_inlineContext):
        pass


    # Enter a parse tree produced by like_rubyParser#pir_expression_list.
    def enterPir_expression_list(self, ctx:like_rubyParser.Pir_expression_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#pir_expression_list.
    def exitPir_expression_list(self, ctx:like_rubyParser.Pir_expression_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition.
    def enterFunction_definition(self, ctx:like_rubyParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition.
    def exitFunction_definition(self, ctx:like_rubyParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_body.
    def enterFunction_definition_body(self, ctx:like_rubyParser.Function_definition_bodyContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_body.
    def exitFunction_definition_body(self, ctx:like_rubyParser.Function_definition_bodyContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_header.
    def enterFunction_definition_header(self, ctx:like_rubyParser.Function_definition_headerContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_header.
    def exitFunction_definition_header(self, ctx:like_rubyParser.Function_definition_headerContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_name.
    def enterFunction_name(self, ctx:like_rubyParser.Function_nameContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_name.
    def exitFunction_name(self, ctx:like_rubyParser.Function_nameContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_params.
    def enterFunction_definition_params(self, ctx:like_rubyParser.Function_definition_paramsContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_params.
    def exitFunction_definition_params(self, ctx:like_rubyParser.Function_definition_paramsContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_params_list.
    def enterFunction_definition_params_list(self, ctx:like_rubyParser.Function_definition_params_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_params_list.
    def exitFunction_definition_params_list(self, ctx:like_rubyParser.Function_definition_params_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_definition_param_id.
    def enterFunction_definition_param_id(self, ctx:like_rubyParser.Function_definition_param_idContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_definition_param_id.
    def exitFunction_definition_param_id(self, ctx:like_rubyParser.Function_definition_param_idContext):
        pass


    # Enter a parse tree produced by like_rubyParser#return_statement.
    def enterReturn_statement(self, ctx:like_rubyParser.Return_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#return_statement.
    def exitReturn_statement(self, ctx:like_rubyParser.Return_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_call.
    def enterFunction_call(self, ctx:like_rubyParser.Function_callContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_call.
    def exitFunction_call(self, ctx:like_rubyParser.Function_callContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_call_param_list.
    def enterFunction_call_param_list(self, ctx:like_rubyParser.Function_call_param_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_call_param_list.
    def exitFunction_call_param_list(self, ctx:like_rubyParser.Function_call_param_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_call_params.
    def enterFunction_call_params(self, ctx:like_rubyParser.Function_call_paramsContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_call_params.
    def exitFunction_call_params(self, ctx:like_rubyParser.Function_call_paramsContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_param.
    def enterFunction_param(self, ctx:like_rubyParser.Function_paramContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_param.
    def exitFunction_param(self, ctx:like_rubyParser.Function_paramContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_unnamed_param.
    def enterFunction_unnamed_param(self, ctx:like_rubyParser.Function_unnamed_paramContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_unnamed_param.
    def exitFunction_unnamed_param(self, ctx:like_rubyParser.Function_unnamed_paramContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_named_param.
    def enterFunction_named_param(self, ctx:like_rubyParser.Function_named_paramContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_named_param.
    def exitFunction_named_param(self, ctx:like_rubyParser.Function_named_paramContext):
        pass


    # Enter a parse tree produced by like_rubyParser#function_call_assignment.
    def enterFunction_call_assignment(self, ctx:like_rubyParser.Function_call_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#function_call_assignment.
    def exitFunction_call_assignment(self, ctx:like_rubyParser.Function_call_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#all_result.
    def enterAll_result(self, ctx:like_rubyParser.All_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#all_result.
    def exitAll_result(self, ctx:like_rubyParser.All_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#elsif_statement.
    def enterElsif_statement(self, ctx:like_rubyParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#elsif_statement.
    def exitElsif_statement(self, ctx:like_rubyParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#if_elsif_statement.
    def enterIf_elsif_statement(self, ctx:like_rubyParser.If_elsif_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#if_elsif_statement.
    def exitIf_elsif_statement(self, ctx:like_rubyParser.If_elsif_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#if_statement.
    def enterIf_statement(self, ctx:like_rubyParser.If_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#if_statement.
    def exitIf_statement(self, ctx:like_rubyParser.If_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#unless_statement.
    def enterUnless_statement(self, ctx:like_rubyParser.Unless_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#unless_statement.
    def exitUnless_statement(self, ctx:like_rubyParser.Unless_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#while_statement.
    def enterWhile_statement(self, ctx:like_rubyParser.While_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#while_statement.
    def exitWhile_statement(self, ctx:like_rubyParser.While_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#for_statement.
    def enterFor_statement(self, ctx:like_rubyParser.For_statementContext):
        pass

    # Exit a parse tree produced by like_rubyParser#for_statement.
    def exitFor_statement(self, ctx:like_rubyParser.For_statementContext):
        pass


    # Enter a parse tree produced by like_rubyParser#init_expression.
    def enterInit_expression(self, ctx:like_rubyParser.Init_expressionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#init_expression.
    def exitInit_expression(self, ctx:like_rubyParser.Init_expressionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#all_assignment.
    def enterAll_assignment(self, ctx:like_rubyParser.All_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#all_assignment.
    def exitAll_assignment(self, ctx:like_rubyParser.All_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#for_init_list.
    def enterFor_init_list(self, ctx:like_rubyParser.For_init_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#for_init_list.
    def exitFor_init_list(self, ctx:like_rubyParser.For_init_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#cond_expression.
    def enterCond_expression(self, ctx:like_rubyParser.Cond_expressionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#cond_expression.
    def exitCond_expression(self, ctx:like_rubyParser.Cond_expressionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#loop_expression.
    def enterLoop_expression(self, ctx:like_rubyParser.Loop_expressionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#loop_expression.
    def exitLoop_expression(self, ctx:like_rubyParser.Loop_expressionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#for_loop_list.
    def enterFor_loop_list(self, ctx:like_rubyParser.For_loop_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#for_loop_list.
    def exitFor_loop_list(self, ctx:like_rubyParser.For_loop_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#statement_body.
    def enterStatement_body(self, ctx:like_rubyParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by like_rubyParser#statement_body.
    def exitStatement_body(self, ctx:like_rubyParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by like_rubyParser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:like_rubyParser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:like_rubyParser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#dynamic_assignment.
    def enterDynamic_assignment(self, ctx:like_rubyParser.Dynamic_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#dynamic_assignment.
    def exitDynamic_assignment(self, ctx:like_rubyParser.Dynamic_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#int_assignment.
    def enterInt_assignment(self, ctx:like_rubyParser.Int_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#int_assignment.
    def exitInt_assignment(self, ctx:like_rubyParser.Int_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#float_assignment.
    def enterFloat_assignment(self, ctx:like_rubyParser.Float_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#float_assignment.
    def exitFloat_assignment(self, ctx:like_rubyParser.Float_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#string_assignment.
    def enterString_assignment(self, ctx:like_rubyParser.String_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#string_assignment.
    def exitString_assignment(self, ctx:like_rubyParser.String_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#table_assignment.
    def enterTable_assignment(self, ctx:like_rubyParser.Table_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#table_assignment.
    def exitTable_assignment(self, ctx:like_rubyParser.Table_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#column_assignment.
    def enterColumn_assignment(self, ctx:like_rubyParser.Column_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#column_assignment.
    def exitColumn_assignment(self, ctx:like_rubyParser.Column_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#row_assignment.
    def enterRow_assignment(self, ctx:like_rubyParser.Row_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#row_assignment.
    def exitRow_assignment(self, ctx:like_rubyParser.Row_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#assignment.
    def enterAssignment(self, ctx:like_rubyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#assignment.
    def exitAssignment(self, ctx:like_rubyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#initial_array_assignment.
    def enterInitial_array_assignment(self, ctx:like_rubyParser.Initial_array_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#initial_array_assignment.
    def exitInitial_array_assignment(self, ctx:like_rubyParser.Initial_array_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#array_assignment.
    def enterArray_assignment(self, ctx:like_rubyParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by like_rubyParser#array_assignment.
    def exitArray_assignment(self, ctx:like_rubyParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by like_rubyParser#array_definition.
    def enterArray_definition(self, ctx:like_rubyParser.Array_definitionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#array_definition.
    def exitArray_definition(self, ctx:like_rubyParser.Array_definitionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#array_definition_elements.
    def enterArray_definition_elements(self, ctx:like_rubyParser.Array_definition_elementsContext):
        pass

    # Exit a parse tree produced by like_rubyParser#array_definition_elements.
    def exitArray_definition_elements(self, ctx:like_rubyParser.Array_definition_elementsContext):
        pass


    # Enter a parse tree produced by like_rubyParser#array_selector.
    def enterArray_selector(self, ctx:like_rubyParser.Array_selectorContext):
        pass

    # Exit a parse tree produced by like_rubyParser#array_selector.
    def exitArray_selector(self, ctx:like_rubyParser.Array_selectorContext):
        pass


    # Enter a parse tree produced by like_rubyParser#dynamic_result.
    def enterDynamic_result(self, ctx:like_rubyParser.Dynamic_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#dynamic_result.
    def exitDynamic_result(self, ctx:like_rubyParser.Dynamic_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#dynamic.
    def enterDynamic(self, ctx:like_rubyParser.DynamicContext):
        pass

    # Exit a parse tree produced by like_rubyParser#dynamic.
    def exitDynamic(self, ctx:like_rubyParser.DynamicContext):
        pass


    # Enter a parse tree produced by like_rubyParser#int_result.
    def enterInt_result(self, ctx:like_rubyParser.Int_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#int_result.
    def exitInt_result(self, ctx:like_rubyParser.Int_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#float_result.
    def enterFloat_result(self, ctx:like_rubyParser.Float_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#float_result.
    def exitFloat_result(self, ctx:like_rubyParser.Float_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#string_result.
    def enterString_result(self, ctx:like_rubyParser.String_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#string_result.
    def exitString_result(self, ctx:like_rubyParser.String_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#table_result.
    def enterTable_result(self, ctx:like_rubyParser.Table_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#table_result.
    def exitTable_result(self, ctx:like_rubyParser.Table_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#column_result.
    def enterColumn_result(self, ctx:like_rubyParser.Column_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#column_result.
    def exitColumn_result(self, ctx:like_rubyParser.Column_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#row_result.
    def enterRow_result(self, ctx:like_rubyParser.Row_resultContext):
        pass

    # Exit a parse tree produced by like_rubyParser#row_result.
    def exitRow_result(self, ctx:like_rubyParser.Row_resultContext):
        pass


    # Enter a parse tree produced by like_rubyParser#comparison_list.
    def enterComparison_list(self, ctx:like_rubyParser.Comparison_listContext):
        pass

    # Exit a parse tree produced by like_rubyParser#comparison_list.
    def exitComparison_list(self, ctx:like_rubyParser.Comparison_listContext):
        pass


    # Enter a parse tree produced by like_rubyParser#comparison.
    def enterComparison(self, ctx:like_rubyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by like_rubyParser#comparison.
    def exitComparison(self, ctx:like_rubyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by like_rubyParser#comp_var.
    def enterComp_var(self, ctx:like_rubyParser.Comp_varContext):
        pass

    # Exit a parse tree produced by like_rubyParser#comp_var.
    def exitComp_var(self, ctx:like_rubyParser.Comp_varContext):
        pass


    # Enter a parse tree produced by like_rubyParser#lvalue.
    def enterLvalue(self, ctx:like_rubyParser.LvalueContext):
        pass

    # Exit a parse tree produced by like_rubyParser#lvalue.
    def exitLvalue(self, ctx:like_rubyParser.LvalueContext):
        pass


    # Enter a parse tree produced by like_rubyParser#rvalue.
    def enterRvalue(self, ctx:like_rubyParser.RvalueContext):
        pass

    # Exit a parse tree produced by like_rubyParser#rvalue.
    def exitRvalue(self, ctx:like_rubyParser.RvalueContext):
        pass


    # Enter a parse tree produced by like_rubyParser#break_expression.
    def enterBreak_expression(self, ctx:like_rubyParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#break_expression.
    def exitBreak_expression(self, ctx:like_rubyParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#literal_t.
    def enterLiteral_t(self, ctx:like_rubyParser.Literal_tContext):
        pass

    # Exit a parse tree produced by like_rubyParser#literal_t.
    def exitLiteral_t(self, ctx:like_rubyParser.Literal_tContext):
        pass


    # Enter a parse tree produced by like_rubyParser#float_t.
    def enterFloat_t(self, ctx:like_rubyParser.Float_tContext):
        pass

    # Exit a parse tree produced by like_rubyParser#float_t.
    def exitFloat_t(self, ctx:like_rubyParser.Float_tContext):
        pass


    # Enter a parse tree produced by like_rubyParser#int_t.
    def enterInt_t(self, ctx:like_rubyParser.Int_tContext):
        pass

    # Exit a parse tree produced by like_rubyParser#int_t.
    def exitInt_t(self, ctx:like_rubyParser.Int_tContext):
        pass


    # Enter a parse tree produced by like_rubyParser#bool_t.
    def enterBool_t(self, ctx:like_rubyParser.Bool_tContext):
        pass

    # Exit a parse tree produced by like_rubyParser#bool_t.
    def exitBool_t(self, ctx:like_rubyParser.Bool_tContext):
        pass


    # Enter a parse tree produced by like_rubyParser#nil_t.
    def enterNil_t(self, ctx:like_rubyParser.Nil_tContext):
        pass

    # Exit a parse tree produced by like_rubyParser#nil_t.
    def exitNil_t(self, ctx:like_rubyParser.Nil_tContext):
        pass


    # Enter a parse tree produced by like_rubyParser#my_id.
    def enterMy_id(self, ctx:like_rubyParser.My_idContext):
        pass

    # Exit a parse tree produced by like_rubyParser#my_id.
    def exitMy_id(self, ctx:like_rubyParser.My_idContext):
        pass


    # Enter a parse tree produced by like_rubyParser#id_global.
    def enterId_global(self, ctx:like_rubyParser.Id_globalContext):
        pass

    # Exit a parse tree produced by like_rubyParser#id_global.
    def exitId_global(self, ctx:like_rubyParser.Id_globalContext):
        pass


    # Enter a parse tree produced by like_rubyParser#id_function.
    def enterId_function(self, ctx:like_rubyParser.Id_functionContext):
        pass

    # Exit a parse tree produced by like_rubyParser#id_function.
    def exitId_function(self, ctx:like_rubyParser.Id_functionContext):
        pass


    # Enter a parse tree produced by like_rubyParser#terminator.
    def enterTerminator(self, ctx:like_rubyParser.TerminatorContext):
        pass

    # Exit a parse tree produced by like_rubyParser#terminator.
    def exitTerminator(self, ctx:like_rubyParser.TerminatorContext):
        pass


    # Enter a parse tree produced by like_rubyParser#else_token.
    def enterElse_token(self, ctx:like_rubyParser.Else_tokenContext):
        pass

    # Exit a parse tree produced by like_rubyParser#else_token.
    def exitElse_token(self, ctx:like_rubyParser.Else_tokenContext):
        pass


    # Enter a parse tree produced by like_rubyParser#crlf.
    def enterCrlf(self, ctx:like_rubyParser.CrlfContext):
        pass

    # Exit a parse tree produced by like_rubyParser#crlf.
    def exitCrlf(self, ctx:like_rubyParser.CrlfContext):
        pass


