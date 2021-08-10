# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PivotTable(Component):
    """A PivotTable component.
...

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- data (list; optional): The input data
- attrClassified (boolean; default False): attrClassified -- whether to show the unused attributes as classfied
- attrCategory (list; optional): attribute list
- unclassifiedAttrName (string; default "Unclassified"): The name of category for attributes that are not in the attrDict
- attrOrder (list; optional): Specify the default order of attributes
- attrLabel (dict; optional): The label should have format of {[attrName]: label}
- selectData (list; optional): selectData -- data selected by cell click
- hiddenAttributes (list; optional): contains attribute names to omit from the UI
- hiddenFromAggregators (list; optional): contains attribute names to omit from the aggregator arguments dropdowns
- hiddenFromDragDrop (list; optional): contains attribute names to omit from the drag'n'drop portion of the UI
- menuLimit (number; default 500): maximum number of values to list in the double-click menu
- unusedOrientationCutoff (number; default 85): If the attributes' names' combined length in characters exceeds this
value then the unused attributes area will be shown vertically to the
left of the UI instead of horizontally above it. 0 therefore means
'always vertical', and Infinity means 'always horizontal'.
- cols (list; optional): Which columns are currently in the column area
- colOrder (string; optional): the order in which column data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by column total
- rows (list; optional): Which rows is currently inside the row area.
- rowOrder (string; optional): the order in which row data is provided to the renderer, must be one
of "key_a_to_z", "value_a_to_z", "value_z_to_a", ordering by value
orders by row total
- aggregatorName (string; optional): Which aggregator is currently selected. E.g. Count, Sum, Average, etc.
- vals (list; optional): Vals for the aggregator.
- valueFilter (dict; optional): Value filter for each attibute name.
- rendererName (string; optional): Which renderer is currently selected. E.g. Table, Line Chart, Scatter
Chart, etc.
- tableOptions (dict; optional): tableOptions -- were clickCallback is placed 
it is a Function to call when mouse clicks on cell
function(e, value, filters, pivotData)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, attrClassified=Component.UNDEFINED, attrCategory=Component.UNDEFINED, unclassifiedAttrName=Component.UNDEFINED, attrOrder=Component.UNDEFINED, attrLabel=Component.UNDEFINED, selectData=Component.UNDEFINED, hiddenAttributes=Component.UNDEFINED, hiddenFromAggregators=Component.UNDEFINED, hiddenFromDragDrop=Component.UNDEFINED, menuLimit=Component.UNDEFINED, unusedOrientationCutoff=Component.UNDEFINED, cols=Component.UNDEFINED, colOrder=Component.UNDEFINED, rows=Component.UNDEFINED, rowOrder=Component.UNDEFINED, aggregatorName=Component.UNDEFINED, vals=Component.UNDEFINED, valueFilter=Component.UNDEFINED, rendererName=Component.UNDEFINED, tableOptions=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'attrClassified', 'attrCategory', 'unclassifiedAttrName', 'attrOrder', 'attrLabel', 'selectData', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop', 'menuLimit', 'unusedOrientationCutoff', 'cols', 'colOrder', 'rows', 'rowOrder', 'aggregatorName', 'vals', 'valueFilter', 'rendererName', 'tableOptions']
        self._type = 'PivotTable'
        self._namespace = 'dash_pivottable'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'attrClassified', 'attrCategory', 'unclassifiedAttrName', 'attrOrder', 'attrLabel', 'selectData', 'hiddenAttributes', 'hiddenFromAggregators', 'hiddenFromDragDrop', 'menuLimit', 'unusedOrientationCutoff', 'cols', 'colOrder', 'rows', 'rowOrder', 'aggregatorName', 'vals', 'valueFilter', 'rendererName', 'tableOptions']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PivotTable, self).__init__(**args)
