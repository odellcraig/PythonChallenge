/* Etch-a-scetch constructor */
function etchAScetch(table, width, height, hMarkSize, vMarkSize) {
    this.table = table;
    this.width = width;
    this.height = height;
    this.hMarkSize = hMarkSize;
    this.vMarkSize = vMarkSize;
    this.drawTable();
}

/* Etch-a-scetch class */
etchAScetch.prototype = {
    width: 16,
    height: 16,
    hMarkSize: 4,
    vMarkSize: 4,
    table: null,
    rowLabels: null,
    colLabels: null,
    cells: null,
    
    drawTable: function() {
        // Logical structure; column groups, table head and table body
        var colGroup = document.createElement('colgroup');
        var labelCol = document.createElement('col');
        labelCol.setAttribute('span', '1');
        labelCol.setAttribute('id', 'row-labels-column');
        colGroup.appendChild(labelCol);
        var restCols = document.createElement('col');
        restCols.setAttribute('span', this.width);
        colGroup.appendChild(restCols);
        this.table.appendChild(colGroup);
        var head = document.createElement('thead');
        this.table.appendChild(head);
        var body = document.createElement('tbody');
        this.table.appendChild(body);

        // Top row, space for column counts
        var labelRow = document.createElement('tr');
        head.appendChild(labelRow);
        var corner = document.createElement('td');
        corner.className = 'corner';
        labelRow.appendChild(corner);
        this.colLabels = new Array(this.width);
        for (var i = 0; i < this.width; i++) {
            var colLabel = document.createElement('th');
            if (i % this.hMarkSize == 0)
                colLabel.className = 'vmarker';
            colLabel.setAttribute('id', 'col-label-' + i);
            labelRow.appendChild(colLabel);
            this.colLabels[i] = colLabel;
        }
        
        // Row labels and cells
        this.rowLabels = new Array(this.height);
        this.cells = new Array();
        for (var j = 0; j < this.height; j++) {
            var row = document.createElement('tr');
            if (j % this.vMarkSize == 0)
                row.className = 'hmarker';
            var rowLabel = document.createElement('th');
            rowLabel.setAttribute('id', 'row-label-' + j);
            row.appendChild(rowLabel);
            this.rowLabels[j] = rowLabel;
            body.appendChild(row);
            var cellRow = new Array();
            this.cells.push(cellRow);
            for (var i = 0; i < this.width; i++) {
                var cell = document.createElement('td');
                cell.className = 'off';
                if (i % this.hMarkSize == 0)
                    cell.className = 'off vmarker';
                cell.setAttribute('id', 'cell-' + i + '-' + j);
                cell.onclick = function() { eas.clickCell(this) };
                row.appendChild(cell);
                cellRow.push(cell);
            }
        }
    },
    
    clickCell: function(cell) {
        var parts = cell.id.split('-');
        var col = parts[1];
        var row = parts[2];

        // Toggle cell class
        var classInfo = cell.className.split(' ');
        if (classInfo[0] == 'on') {
            classInfo[0] = 'off';
        } else {
            classInfo[0] = 'on';
        }
        cell.className = classInfo.join(' ');
        
        // Count cell groups
        this.setRowLabel(row, this.countRow(row));
        this.setColLabel(col, this.countCol(col));
    },
    
    setRowLabel: function(row, counts) {
        this.rowLabels[row].innerHTML = '<nobr>' + counts.join(' ') + '</nobr>';
    },
    
    setColLabel: function(col, counts) {
        this.colLabels[col].innerHTML = counts.join('<br />');
    },
    
    countRow: function(row) {
        var counts = new Array();
        var count = 0;
        for (var i = 0; i < this.width; i++) {
            var cell = this.cells[row][i];
            var classNames = cell.className.split(' ');
            if (classNames[0] == 'on') {
                count = count + 1;
            } else {
                if (count > 0)
                    counts.push(count);
                count = 0;
            }
        }
        if (count > 0)
            counts.push(count);
        return counts;
    },
    
    countCol: function(col) {
        var counts = new Array();
        var count = 0;
        for (var j = 0; j < this.height; j++) {
            var cell = this.cells[j][col];
            var classNames = cell.className.split(' ');
            if (classNames[0] == 'on') {
                count = count + 1;
            } else {
                if (count > 0)
                    counts.push(count);
                count = 0;
            }
        }
        if (count > 0)
            counts.push(count);
        return counts;
    },
    
    loadImage: function(pixels) {
        for (var i = 0; i < pixels.length; i++) {
            col = pixels[i][0];
            row = pixels[i][1];
            var cell = this.cells[row][col];
            var classNames = cell.className.split(' ');
            classNames[0] = 'on';
            cell.className = classNames.join(' ');
        }
        for (var c = 0; c < this.width; c++)
            this.setColLabel(c, this.countCol(c));
        for (var r = 0; r < this.height; r++)
            this.setRowLabel(r, this.countRow(r));
    }
}
