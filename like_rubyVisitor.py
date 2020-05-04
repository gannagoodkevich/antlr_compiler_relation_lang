# Generated from like_ruby.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .like_rubyParser import like_rubyParser
else:
    from like_rubyParser import like_rubyParser

# This class defines a complete generic visitor for a parse tree produced by like_rubyParser.

class like_rubyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by like_rubyParser#prog.
    def visitProg(self, ctx:like_rubyParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#function_definition_list.
    def visitFunction_definition_list(self, ctx:like_rubyParser.Function_definition_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#expression_list.
    def visitExpression_list(self, ctx:like_rubyParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#expression.
    def visitExpression(self, ctx:like_rubyParser.ExpressionContext):
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


    # Visit a parse tree produced by like_rubyParser#require_block.
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#function_definition_body.
    def visitFunction_definition_body(self, ctx:like_rubyParser.Function_definition_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#function_definition_header.
    def visitFunction_definition_header(self, ctx:like_rubyParser.Function_definition_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#function_name.
    def visitFunction_name(self, ctx:like_rubyParser.Function_nameContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#float_assignment.
    def visitFloat_assignment(self, ctx:like_rubyParser.Float_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#string_assignment.
    def visitString_assignment(self, ctx:like_rubyParser.String_assignmentContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by like_rubyParser#rvalue.
    def visitRvalue(self, ctx:like_rubyParser.RvalueContext):
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



del like_rubyParser